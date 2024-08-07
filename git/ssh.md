# SSH

### SSH概念

SSH（Secure Shell）是一种用于安全登录到远程计算机和执行命令的协议。

- **基本连接：**
  ```bash
  ssh username@hostname
  ```
  连接到指定的远程主机。

- **指定端口：**
  ```bash
  ssh -p port_number username@hostname
  ```
  连接到指定端口的远程主机。

- **公钥认证：**
  生成SSH密钥对：
  ```bash
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```
  将公钥复制到远程服务器：
  ```bash
  ssh-copy-id username@hostname
  ```

- **文件传输：**
  使用SCP传输文件：
  ```bash
  scp local_file username@hostname:/remote/directory
  ```
  使用SFTP传输文件：
  ```bash
  sftp username@hostname
  ```

### git ssh 连接

首先要确保设置了git的用户名与邮箱

```shell
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

通过以下命令验证配置是否成功

```bash
git config --global user.name
git config --global user.email
```

生成ssh密钥

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

启动ssh代理（windows可以用 Git Bash）

```bash
eval "$(ssh-agent -s)"
```

将您的ssh私钥添加到ssh代理中

```bash
ssh-add ~/.ssh/id_rsa
```

显示公钥内容，并手动复制

```bash
cat ~/.ssh/id_rsa.pub
```

添加公钥到Git托管服务

- **GitHub:**
  - 登录到GitHub
  - 进入**Settings（设置）**
  - 选择**SSH and GPG keys**
  - 点击**New SSH key**
  - 粘贴您的公钥到**Key**字段中，并给它一个**Title（标题）**
  - 点击**Add SSH key**

测试Github，您可以在终端中运行：

```bash
ssh -T git@github.com
```

如果连接成功，您将看到一条欢迎信息，如：

```scss
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

查看当前远程URL

在仓库目录中，使用以下命令查看当前的远程URL：

```bash
git remote -v
```

您可能会看到如下输出：

```scss
origin  https://github.com/username/repository.git (fetch)
origin  https://github.com/username/repository.git (push)
```

更改远程URL为SSH

使用以下命令更改远程URL为SSH：

```bash
git remote set-url origin git@github.com:username/repository.git
```

验证更改

再次查看远程URL以确认更改成功：

```bash
git remote -v
```

您应该会看到类似如下的输出：

```scss
origin  git@github.com:username/repository.git (fetch)
origin  git@github.com:username/repository.git (push)
```