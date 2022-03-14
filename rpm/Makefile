make_rpm: clean
	yum install -y rpmdevtools rpmlint git python3
	rpmdev-setuptree
	cd ~/rpmbuild/BUILD && git clone https://github.com/ampledata/spotcot.git spotcot-0.0.1
	cd ~/rpmbuild/BUILD && tar --create --file spotcot-0.0.1.tar.gz spotcot-0.0.1 && mv -f spotcot-0.0.1.tar.gz ../SOURCES/
	cp spotcot.spec ~/rpmbuild/SPECS
	rpmbuild -bb ~/rpmbuild/SPECS/spotcot.spec
	echo
	@echo "**********************************************************************************************"
	@echo "Use below command to install RPM using yum package manage"
	@echo "yum install `find ~/rpmbuild -iname *.rpm`"
	@echo "**********************************************************************************************"
	@echo

clean:
	rm -rf ~/rpmbuild
