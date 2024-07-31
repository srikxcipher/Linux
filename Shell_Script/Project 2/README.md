# Checkout before Running the Main script.

# Postfix and Mailx Installation & Configuration Guide

This guide provides instructions for installing and configuring Postfix and Mailx on CentOS/RHEL and Ubuntu systems.

## 1. Install Dependencies

### For CentOS/RHEL

1. **Update Your System**
    ```bash
    sudo yum update
    ```

2. **Install Postfix**
    ```bash
    sudo yum install postfix
    ```

3. **Install Mailx**
    ```bash
    sudo yum install mailx
    ```

### For Ubuntu

1. **Update Your System**
    ```bash
    sudo apt update
    ```

2. **Install Postfix**
    ```bash
    sudo apt install postfix
    ```

3. **Install Mailx**
    ```bash
    sudo apt install mailx
    ```

## 2. Verify Installation

### For Red Hat-Based Systems (CentOS, Fedora)

- **Check if Postfix is Installed**
    ```bash
    rpm -q postfix
    ```

- **Check if Mailx is Installed**
    ```bash
    rpm -q mailx
    ```

### For Debian-Based Systems (Ubuntu)

- **Check if Postfix is Installed**
    ```bash
    dpkg -l | grep postfix
    ```

- **Check if Mailx is Installed**
    ```bash
    dpkg -l | grep mailx
    ```

- **Alternatively, Check with APT**
    ```bash
    apt list --installed | grep postfix
    apt list --installed | grep mailx
    ```

## 3. Postfix Configuration

1. **Open the Configuration File**
    ```bash
    sudo nano /etc/postfix/main.cf
    ```

2. **Basic Configuration**

    Update the following settings in `main.cf`:

    ```plaintext
    myhostname = mail.example.com
    mydomain = example.com
    myorigin = $mydomain
    mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
    relayhost =
    mynetworks = 127.0.0.0/8, [::1]/128
    mailbox_size_limit = 0
    recipient_delimiter = +
    smtpd_relay_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination
    ```

## 4. Additional Configuration

### TLS/SSL

To enable TLS/SSL, add the following to `main.cf`:

```plaintext
smtpd_tls_cert_file = /etc/ssl/certs/ssl-cert-snakeoil.pem
smtpd_tls_key_file = /etc/ssl/private/ssl-cert-snakeoil.key
smtpd_use_tls = yes
smtpd_tls_security_level = may
smtpd_tls_loglevel = 1
```
## 5. Post-Configuration Steps

**Reload Postfix**
```plaintext
sudo systemctl reload postfix
```
**Check Postfix Status**
```plaintext
sudo systemctl status postfix
```
**Check Mailx Status**
```plaintext
sudo systemctl status mailx
```
**Test Your Configuration**
```plaintext
echo "This is a test email body" | mail -s "Test Subject" recipient@example.com
```


## 6. Monitor Logs

**To view mail logs and troubleshoot issues, use:**
```plaintext
sudo tail -f /var/log/mail.log
```

### Refer to the Postfix documentation for more advanced configurations

[Postfix doc ⚙️](https://www.postfix.org/documentation.html)


