Summary:	Proof General, Emacs interface for Proof Assistants
Name:		ProofGeneral
Version:	3.3pre001220
Release:	1
Group:		Applications/Editors/Emacs
Copyright:	LFCS, University of Edinburgh
Url:		http://www.proofgeneral.org/
Packager:	David Aspinall <da@dcs.ed.ac.uk>
Source:		http://www.proofgeneral.org/ProofGeneral-3.3pre001220.tar.gz
BuildRoot:	/tmp/ProofGeneral-root
Patch:		ProofGeneral.patch
PreReq:		/sbin/install-info
Prefixes:	/usr/share/emacs /usr/bin /usr/info
BuildArchitectures: noarch

%description
Proof General is a generic Emacs interface for proof assistants,
suitable for use by pacifists and Emacs militants alike.
It is supplied ready-customized for LEGO, Coq, and Isabelle.
You can adapt Proof General to other proof assistants if you know a
little bit of Emacs Lisp.

To use Proof General, use the command `proofgeneral', which launches
XEmacs (or Emacs) for you, or add the line:

   (load-file "/usr/share/emacs/ProofGeneral/generic/proof-site.el")

to your .emacs file so Proof General is available whenever 
you run Emacs.

%changelog
* Thu Dec  7 2000 David Aspinall <da@dcs.ed.ac.uk> 
- Name change af2 -> phox

* Fri Sep 29 2000 David Aspinall <da@dcs.ed.ac.uk> 
- For 3.2, add more provers (af2, acl2, twelf).  Added proofgeneral script.

* Mon Mar 13 2000 David Aspinall <da@dcs.ed.ac.uk>
- For 3.1, added hol98 instance.

* Wed Aug 25 1999 David Aspinall <da@dcs.ed.ac.uk>
- For 2.1 and 2.2pre series: made relocatable, added isar/ to package.

* Thu Sep 24 1998 David Aspinall <da@dcs.ed.ac.uk>
- First version.

%prep
%setup
%patch -p0
rm -f */*.orig

%build

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/share/emacs/ProofGeneral

# Put binaries in proper place
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mv bin/proofgeneral lego/legotags coq/coqtags ${RPM_BUILD_ROOT}/usr/bin

# Put info file in proper place, compress it.
mkdir -p ${RPM_BUILD_ROOT}/usr/info
mv doc/ProofGeneral.info doc/ProofGeneral.info-* ${RPM_BUILD_ROOT}/usr/info
mv doc/PG-adapting.info  doc/PG-adapting.info-*  ${RPM_BUILD_ROOT}/usr/info
gzip ${RPM_BUILD_ROOT}/usr/info/ProofGeneral.info  ${RPM_BUILD_ROOT}/usr/info/ProofGeneral.info-*
gzip ${RPM_BUILD_ROOT}/usr/info/PG-adapting.info ${RPM_BUILD_ROOT}/usr/info/PG-adapting.info-*
# Remove duff bits
rm -f doc/dir doc/localdir 

cp -pr phox acl2 twelf coq lego isa isar hol98 images generic ${RPM_BUILD_ROOT}/usr/share/emacs/ProofGeneral


%clean
if [ "X" != "${RPM_BUILD_ROOT}X" ]; then
    rm -rf $RPM_BUILD_ROOT
fi

%post
/sbin/install-info /usr/info/ProofGeneral.info.gz /usr/info/dir
/sbin/install-info /usr/info/PG-adapting.info.gz /usr/info/dir

%preun
/sbin/install-info --delete /usr/info/ProofGeneral.info.gz /usr/info/dir
/sbin/install-info --delete /usr/info/PG-adapting.info.gz /usr/info/dir

%files
%attr(-,root,root) %doc AUTHORS BUGS CHANGES COPYING INSTALL README README.devel doc/* 
%attr(-,root,root) /usr/info/ProofGeneral.info.*
%attr(-,root,root) /usr/info/ProofGeneral.info-*.*
%attr(-,root,root) /usr/info/PG-adapting.info.*
%attr(-,root,root) /usr/info/PG-adapting.info-*.*
%attr(-,root,root) /usr/bin/proofgeneral
%attr(-,root,root) /usr/bin/coqtags
%attr(-,root,root) /usr/bin/legotags
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/coq
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/coq/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/coq/*.v
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/lego
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/lego/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/lego/*.l
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/isa
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/isa/interface
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/isa/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/isa/*.thy
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/isa/*.ML
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/isar
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/isar/interface
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/isar/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/isar/*.thy
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/hol98
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/hol98/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/hol98/*.sml
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/phox
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/phox/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/phox/*.phx
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/acl2
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/acl2/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/acl2/*.acl2
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/twelf
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/twelf/*.el
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/twelf/*.elf
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/images
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/images/*
%attr(0755,root,root) %dir /usr/share/emacs/ProofGeneral/generic
%attr(-,root,root) %dir /usr/share/emacs/ProofGeneral/generic/*.el
