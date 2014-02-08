# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/examdesign
# catalog-date 2006-12-09 23:51:48 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-examdesign
Version:	20061209
Release:	3
Summary:	LaTeX class for typesetting exams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/examdesign
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/examdesign.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/examdesign.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/examdesign.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides a class examdesign. The class provides
several features useful for designing tests or question sets: -
it allows for explicit markup of questions and answers; - the
class will, at the user's request, automatically generate
answer keys; - multiple versions of the same test can be
generated automatically, with the ordering of questions within
each section randomly permuted so as to minimize cheating; -
the generated answer keys can be constructed either with or
without the questions included; - environments are provided to
assist in constructing the most common types of test question:
matching, true/false, multiple-choice, fill-in-the-blank, and
short answer/essay questions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/examdesign/examdesign.cls
%doc %{_texmfdistdir}/doc/latex/examdesign/Bugs
%doc %{_texmfdistdir}/doc/latex/examdesign/Changes
%doc %{_texmfdistdir}/doc/latex/examdesign/INSTALL
%doc %{_texmfdistdir}/doc/latex/examdesign/README
%doc %{_texmfdistdir}/doc/latex/examdesign/examdesign.pdf
%doc %{_texmfdistdir}/doc/latex/examdesign/examplea.pdf
%doc %{_texmfdistdir}/doc/latex/examdesign/examplea.tex
%doc %{_texmfdistdir}/doc/latex/examdesign/exampleb.pdf
%doc %{_texmfdistdir}/doc/latex/examdesign/exampleb.tex
%doc %{_texmfdistdir}/doc/latex/examdesign/examplec.pdf
%doc %{_texmfdistdir}/doc/latex/examdesign/examplec.tex
%doc %{_texmfdistdir}/doc/latex/examdesign/foobar.tex
#- source
%doc %{_texmfdistdir}/source/latex/examdesign/examdesign.dtx
%doc %{_texmfdistdir}/source/latex/examdesign/examdesign.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061209-2
+ Revision: 751672
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061209-1
+ Revision: 718395
- texlive-examdesign
- texlive-examdesign
- texlive-examdesign
- texlive-examdesign

