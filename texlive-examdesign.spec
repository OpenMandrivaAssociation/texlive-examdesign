%global tl_name examdesign
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.101
Release:	%{tl_revision}.1
Summary:	LaTeX class for typesetting exams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/examdesign
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/examdesign.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/examdesign.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/examdesign.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides a class examdesign. The class provides several
features useful for designing tests or question sets: it allows for
explicit markup of questions and answers; the class will, at the user's
request, automatically generate answer keys; multiple versions of the
same test can be generated automatically, with the ordering of questions
within each section randomly permuted so as to minimize cheating; the
generated answer keys can be constructed either with or without the
questions included; environments are provided to assist in constructing
the most common types of test question: matching, true/false, multiple-
choice, fill-in-the-blank, and short answer/essay questions.

