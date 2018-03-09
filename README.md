# goss-rpm
Build GOSS with GO and package with RPM!

##
Please note: This is *not* a fork of goss. Please refer to the goss github for details on
goss https://goss.rocks. What this project provides is simple instructions for building
goss on CentOS 7, an RPM specfile for building a goss package, and a couple of sample
YAML files for running goss.

##
Install go and glide:

    # yum install golang-bin 
    # yum install glide

##
Build goss with go:

```# sudo yum -y install glide golang-bin
# go get github.com/aelsabbahy/goss
# export GOBIN=~/go/bin/
# go install go/src/github.com/aelsabbahy/goss/cmd/goss/goss.go
# go/bin/goss
```

##
Build a goss RPM:

```# sudo yum install rpm-build
# mkdir -p {~/rpmbuild,~/rpmbuild/SPECS,~/rpmbuild/SOURCES}
# cp goss.base.yaml goss.service goss.webserver.yaml ~/rpmbuild/SOURCES
# cp goss.spec ~/rpmbuild/SPECS
```

_Modify goss.spec as needed_

Include the following in ~/.rpmmacros:

```%_sysconfdir  /usr/local/etc
%_prefix            /usr/local
%_exec_prefix       %{_prefix}
%_bindir            %{_exec_prefix}/bin
```
And build the RPM: 

```# cd ~/rpmbuild/SPECS
# rpmbuild -bb goss.spec
```
