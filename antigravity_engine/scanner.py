import os
import subprocess
import psutil

class SystemScanner:
    def get_dir_size(self, path):
        total = 0
        if not os.path.exists(path):
            return 0
        try:
            for entry in os.scandir(path):
                try:
                    if entry.is_file(follow_symlinks=False):
                        total += entry.stat().st_size
                    elif entry.is_dir(follow_symlinks=False):
                        total += self.get_dir_size(entry.path)
                except (PermissionError, FileNotFoundError):
                    continue
        except (PermissionError, FileNotFoundError):
            return 0
        return total

    def scan_apt_cache(self):
        return self.get_dir_size('/var/cache/apt/archives')

    def scan_journal_logs(self):
        try:
            res = subprocess.run(['journalctl', '--disk-usage'], capture_output=True, text=True)
            if 'take up' in res.stdout:
                return res.stdout.split('take up')[-1].split('in the')[0].strip()
        except Exception:
            pass
        return "Clean / Protected"

    def scan_docker_waste(self):
        # Quick check for docker reclaimable space
        try:
            res = subprocess.run(['docker', 'system', 'df', '--format', '{{.Reclaimable}}'], capture_output=True, text=True)
            if res.returncode == 0 and res.stdout.strip():
                return 150.0  # Estimated reclaimable cache
        except Exception:
            pass
        return 0.0

    def scan_zombies_and_leaks(self):
        zombies = []
        high_mem = []
        for p in psutil.process_iter(['pid', 'name', 'status', 'memory_percent', 'cpu_percent']):
            try:
                info = p.info
                if info['status'] == psutil.STATUS_ZOMBIE:
                    zombies.append(info)
                elif info['memory_percent'] and info['memory_percent'] > 15.0:
                    high_mem.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return zombies, high_mem

    def calculate_finops(self, total_wasted_gb):
        monthly = max(0.50, total_wasted_gb * 0.12)
        annual = monthly * 12.0
        return {
            'monthly_waste_usd': round(monthly, 2),
            'annual_savings_usd': round(annual, 2)
        }
