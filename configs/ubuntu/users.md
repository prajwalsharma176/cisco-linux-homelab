# Linux User and Group Management

## Purpose

Linux user and group management is used to control authentication, authorization, and administrative privileges on the Ubuntu Server. User accounts and groups are managed following standard Linux administration practices.

---

## Current User

The primary administrative user is:

```text
prajwal
```

Verification:

```bash
whoami
```

Output:

```text
prajwal
```

---

## User Information

User details were verified using:

```bash
id
```

Output:

```text
uid=1000(prajwal)
gid=1000(prajwal)
groups=1000(prajwal),27(sudo),100(users)
```

Summary:

| Property | Value |
|----------|-------|
| Username | prajwal |
| User ID (UID) | 1000 |
| Primary Group | prajwal (GID 1000) |
| Supplementary Groups | sudo, users |

---

## Group Membership

Current group membership:

| Group | Purpose |
|--------|---------|
| sudo | Administrative privileges using sudo |
| users | Standard Linux user group |
| prajwal | Primary user group |

Verification:

```bash
groups
```

Output:

```text
prajwal sudo users
```

---

## Administrative Commands

Display current user:

```bash
whoami
```

Display user information:

```bash
id
```

Display group membership:

```bash
groups
```

Create a new user:

```bash
sudo adduser <username>
```

Grant administrative privileges:

```bash
sudo usermod -aG sudo <username>
```

Change a user's password:

```bash
passwd <username>
```

---

## File Ownership and Permissions

Common Linux permission commands:

```bash
ls -l
chmod
chown
chgrp
```

These commands are used to manage file ownership, group ownership, and file permissions on the server.

---

## Security Notes

- Administrative operations are performed using the `sudo` group.
- User and group information is verified using standard Linux commands.
- File ownership and permissions follow standard Linux security practices.
- Authentication and authorization are managed through Linux user and group accounts.

---

## References

```text
man adduser
man usermod
man passwd
man groups
man id
```