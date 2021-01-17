import subprocess


# Python script to execute commands in terminal

def main():        
    try:
        cmd = "git"
        params = ["init"]
        ps = ""
        for p in params:
            ps +=str(p)            
        print("Executing command : "+cmd+" "+ps)
        subprocess.check_call([cmd, ps])
        
    except subprocess.CalledProcessError as e:
        print(e.output)

if __name__ == '__main__':
    main()    