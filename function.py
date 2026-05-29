import shutil
import subprocess
import os

def check():
    os.system("clear")

    status = 0
    print("""
  _____         _   _                   
 |_   _|__  ___| |_(_)_ __   __ _       
   | |/ _ \/ __| __| | '_ \ / _` |      
   | |  __/\__ \ |_| | | | | (_| |_ _ _ 
   |_|\___||___/\__|_|_| |_|\__, (_|_|_)
                            |___/        
          """)
    docker = shutil.which("docker")
    cloudflared = shutil.which("cloudflared")

    print("cek semua hal yang dibutuhkan...")
    if docker:
        try:
            docker_ping = subprocess.run(
                    ["docker", "ps"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=True,
                )
            print("Daemon Docker : Berjalan")
        except(subprocess.CalledProcessError, FileNotFoundError):
            print("Daemon Docker : Tidak merespon")
            status += 1
    else:
        print("Docker Belum Terinstall")
        status += 1

    if cloudflared:
        try:
            cloudflared_test = subprocess.run(
                    ["cloudflared","--version"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=True,
                )
            print("Cloudflared : Berjalan!")
        except(subprocess.CalledProcessError, FileNotFoundError):
            print("CloudFlared : Tidak merespon")
            status += 1
    else:
        print("Cloudflared belum terinstall")
        status += 1

    if status == 0:
        print("""
  ____       _                 _
 / ___|  ___| | ___  ___  __ _(_)
 \___ \ / _ \ |/ _ \/ __|/ _` | |
  ___) |  __/ |  __/\__ \ (_| | |  _ _ _
 |____/ \___|_|\___||___/\__,_|_| (_|_|_)

         """)
        return 0
    else:
        print("""
  _____                     _
 | ____|_ __ _ __ ___  _ __| |
 |  _| | '__| '__/ _ \| '__| |
 | |___| |  | | | (_) | |  |_|
 |_____|_|  |_|  \___/|_|  (_)
        """)
        return 1

def listService():
    print('work')
    lss = subprocess.run(["docker", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
    print(lss.stdout)

if __name__ == "__main__":
    check()

