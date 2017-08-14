AC_PREREQ(2.52)

AC_INIT([chkchn], [0.1.0], [francis.tyers@uit.no])
AM_INIT_AUTOMAKE([chkchn], [0.1.0], no-define)
AC_PROG_LN_S
AC_PROG_AWK

AC_PATH_PROG([HFSTLEXC], [hfst-lexc], [false], [$PATH$PATH_SEPARATOR$with_hfst_lexc/bin])
AS_IF([test x$HFSTLEXC = xfalse], [AC_MSG_ERROR([You don't have hfst-lexc installed])])

AC_PATH_PROG([HFSTTWOLC], [hfst-twolc], [false], [$PATH$PATH_SEPARATOR$with_hfst_twolc/bin])
AS_IF([test x$HFSTTWOLC = xfalse], [AC_MSG_ERROR([You don't have hfst-twolc installed])])

AP_MKINCLUDE

AC_OUTPUT([Makefile])
