# Generated from yajl-ruby-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname yajl-ruby
%define version 1.1.0
%define release 2
%define debug_package %{nil}

Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://github.com/brianmario/yajl-ruby
Source0: http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.6
Requires: rubygems >= 1.8
Requires: rubygem-rake-compiler >= 0.7.5
Requires: rubygem-rspec >= 2.0.0
Requires: rubygem-activesupport 
Requires: rubygem-json 
BuildRequires: ruby >= 1.8.6
BuildRequires: yajl-devel
BuildRequires: ruby-devel
BuildRequires: rubygems
Provides: rubygem(yajl-ruby) = %{version}

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gembuilddir %{buildroot}%{gemdir}

%description

%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
mkdir -p .%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gemdir} --force %{SOURCE0}
mv .%{gemdir}/*  %{gembuilddir}/
%{__rm} -rf %{gembuilddir}/gems/%{rbname}-%{version}/ext
%{__rm} -f %{gembuilddir}/gems/%{rbname}-%{version}/.{gitignore,rspec,travis.yml}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/yajl-ruby-%{version}/CHANGELOG.md
%{gemdir}/gems/yajl-ruby-%{version}/Gemfile
%{gemdir}/gems/yajl-ruby-%{version}/MIT-LICENSE
%{gemdir}/gems/yajl-ruby-%{version}/README.md
%{gemdir}/gems/yajl-ruby-%{version}/Rakefile
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/encode.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/encode_json_and_marshal.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/encode_json_and_yaml.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/http.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/parse.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/parse_json_and_marshal.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/parse_json_and_yaml.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/parse_stream.rb
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/subjects/item.json
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/subjects/ohai.json
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/subjects/ohai.marshal_dump
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/subjects/ohai.yml
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/subjects/twitter_search.json
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/subjects/twitter_stream.json
%{gemdir}/gems/yajl-ruby-%{version}/benchmark/subjects/unicode.json
%{gemdir}/gems/yajl-ruby-%{version}/examples/encoding/chunked_encoding.rb
%{gemdir}/gems/yajl-ruby-%{version}/examples/encoding/one_shot.rb
%{gemdir}/gems/yajl-ruby-%{version}/examples/encoding/to_an_io.rb
%{gemdir}/gems/yajl-ruby-%{version}/examples/http/twitter_search_api.rb
%{gemdir}/gems/yajl-ruby-%{version}/examples/http/twitter_stream_api.rb
%{gemdir}/gems/yajl-ruby-%{version}/examples/parsing/from_file.rb
%{gemdir}/gems/yajl-ruby-%{version}/examples/parsing/from_stdin.rb
%{gemdir}/gems/yajl-ruby-%{version}/examples/parsing/from_string.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/bzip2.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/bzip2/stream_reader.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/bzip2/stream_writer.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/deflate.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/deflate/stream_reader.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/deflate/stream_writer.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/gzip.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/gzip/stream_reader.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/gzip/stream_writer.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/http_stream.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/json_gem.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/json_gem/encoding.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/json_gem/parsing.rb
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/version.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/encoding/encoding_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/global/global_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/fixtures/http.bzip2.dump
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/fixtures/http.chunked.dump
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/fixtures/http.deflate.dump
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/fixtures/http.error.dump
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/fixtures/http.gzip.dump
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/fixtures/http.html.dump
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/fixtures/http.raw.dump
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/http_delete_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/http_error_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/http_get_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/http_post_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/http_put_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/http/http_stream_options_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/json_gem_compatibility/compatibility_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/active_support_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/chunked_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail.15.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail.16.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail.17.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail.26.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail11.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail12.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail13.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail14.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail19.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail20.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail21.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail22.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail23.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail24.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail25.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail27.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail28.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail3.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail4.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail5.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail6.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/fail9.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.array.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.codepoints_from_unicode_org.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.contacts.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.db100.xml.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.db1000.xml.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.dc_simple_with_comments.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.deep_arrays.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.difficult_json_c_test_case.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.difficult_json_c_test_case_with_comments.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.doubles.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.empty_array.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.empty_string.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.escaped_bulgarian.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.escaped_foobar.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.item.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.json-org-sample1.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.json-org-sample2.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.json-org-sample3.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.json-org-sample4-nows.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.json-org-sample4.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.json-org-sample5.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.map-spain.xml.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.ns-invoice100.xml.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.ns-soap.xml.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.numbers-fp-4k.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.numbers-fp-64k.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.numbers-int-4k.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.numbers-int-64k.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.twitter-search.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.twitter-search2.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.unicode.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass.yelp.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass1.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass2.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures/pass3.json
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/fixtures_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/parsing/one_off_spec.rb
%{gemdir}/gems/yajl-ruby-%{version}/spec/rcov.opts
%{gemdir}/gems/yajl-ruby-%{version}/spec/spec_helper.rb
%{gemdir}/gems/yajl-ruby-%{version}/tasks/compile.rake
%{gemdir}/gems/yajl-ruby-%{version}/tasks/rspec.rake
%{gemdir}/gems/yajl-ruby-%{version}/yajl-ruby.gemspec
%{gemdir}/gems/yajl-ruby-%{version}/lib/yajl/yajl.so


%doc %{gemdir}/doc/yajl-ruby-%{version}
%{gemdir}/cache/yajl-ruby-%{version}.gem
%{gemdir}/specifications/yajl-ruby-%{version}.gemspec

%changelog
* Tue Sep 11 2012 Sergio Rubio <rubiojr@frameos.org> - 1.1.0-1
- initial release

