FROM centos:7

# 安装 Git 和 Jenkins 的依赖
RUN yum install -y java-11-openjdk-devel git wget

# 下载并安装 Jenkins
RUN wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
RUN yum install -y jenkins

# 启动 Jenkins 服务
CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war"]
