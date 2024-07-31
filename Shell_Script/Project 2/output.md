# Steps

## 1. Locate File

To locate the file, use locate command and <file_name>:

> **Command:**
> ```plaintext
> locate fs_status.sh
> ```

**After getting the Path, move to file directory**

> **Path:**
> 
> ```plaintext
> cd /home/user/projects/fs_status.sh
> ```

## 2. Run It

Execute the following command to run the file:

> **Command:**
> 
> ```bash
>  bash fs_status.sh
> ```

## 3. Result

The expected output or result from running the file will be:

> **Result:**
> 
> ```plaintext
> [user@centos01 projects]$ bash fs_status.sh
> ```
> 
> **Check Your Inbox 📧**
>
>![Alt Text](https://github.com/srikxcipher/Linux/blob/ab1dd40b694c08627c8b5d1a0394cf7d75e7c591/Shell_Script/Project%202/assets/IMG_20240731_095458.jpg)
>
> 
> **Verify mail status 📝**
> 
> **Check logs:**
> ```bash
> [user@centos01 projects]$ sudo grep recipient@example.com /var/log/mail.log
> 
>
> for CentOS/RHEL:
> [user@centos01 projects]$ sudo grep recipient@example.com /var/log/maillog
>
> 
> You can also use tail to monitor logs in real-time:
> [user@centos01 projects]$ sudo tail -f /var/log/mail.log
>
> 
> for CentOS/RHEL:
> [user@centos01 projects]$ sudo tail -f /var/log/maillog
> ```
