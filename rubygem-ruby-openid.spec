%global gem_name ruby-openid

Name: rubygem-%{gem_name}
Version: 2.5.0
Release: 2%{?dist}
Summary: A library for consuming and serving OpenID identities
Group: Development/Languages
# License breakdown:
#  Ruby and ASL 2.0:
#   lib/hmac/hmac.rb and lib/openid/yadis/htmltokenizer.rb
#  MIT:
#   Prototype JS at examples/rails_openid/public/javascripts/
#  LGPLv2+ in test suite (not shipped in RPM):
#   https://github.com/openid/ruby-openid/issues/64
License: Ruby and ASL 2.0 and MIT
URL: https://github.com/openid/ruby-openid
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# This package was renamed from "ruby-openid".
# Provide the necessary compatibility bits on older Fedoras.
%if 0%{?fedora} && 0%{?fedora} < 22
Provides:  ruby-openid  = %{version}-%{release}
Provides:  ruby(openid) = %{version}-%{release}
Obsoletes: ruby-openid  <= 2.1.7-11
Obsoletes: ruby(openid) <= 2.1.7-11
%endif

%description
The Ruby OpenID library, with batteries included.

A Ruby library for verifying and serving OpenID identities.
Ruby OpenID makes it easy to add OpenID authentication to
your web applications.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%if 0%{?fedora} && 0%{?fedora} < 22
Provides:  ruby-openid-doc  = %{version}-%{release}
Obsoletes: ruby-openid-doc  <= 2.1.7-11
%endif

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

# Adjust permissions
find ./examples -name \*.rb -print0 | xargs -0 chmod 0644

# Remove /usr/bin/env from shebang so RPM doesn't consider this a dependency
for f in examples/rails_openid/script/rails examples/discover; do
  sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' $f
done

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
# https://github.com/openid/ruby-openid/issues/60
export LANG=en_US.utf8
pushd .%{gem_instdir}
  testrb -Ilib test
popd


%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%exclude %{gem_instdir}/INSTALL.md
%doc %{gem_instdir}/NOTICE
%doc %{gem_instdir}/UPGRADE.md
%{gem_instdir}/examples
%exclude %{gem_instdir}/test


%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.5.0-1
- Update to ruby-openid 2.5.0 (RHBZ #1059660)

* Tue Oct 29 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.3.0-4
- Add obsoletes/provides for -doc subpackage (satisfies depcheck)

* Sun Oct 27 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.3.0-3
- Updates for review request (RHBZ #1015778)
- Update obsoletes
- Update license
- Remove /usr/bin/env from -doc auto-requires

* Thu Oct 24 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.3.0-2
- Updates for review request (RHBZ #1015778)
- Update license
- Clean up whitespace
- Adjust permissions on "examples" directory
- Add link to upstream test suite encoding bug
- Move README.md to main package
- Exclude INSTALL.md file and "test" directory

* Sat Oct 05 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.3.0-1
- Update to 2.3.0
- Remove BR: ruby, since BR: ruby(release) does the same thing
- Set proper Obsoletes/Provides
- Enable test suite

* Mon Aug 19 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.2.3-1
- Initial package

