@ECHO ON
REM ������������� ���������� ��������� ��� ������� PostgreSQL
@SET PATH="%CD%\bin";%PATH%
@SET PGDATA=%CD%\data
@SET PGDATABASE=postgres
@SET PGUSER=postgres
@SET PGPORT=5439
@SET PGLOCALEDIR=%CD%\share\locale
REM %CD%\bin\initdb -U postgres -A trust
%CD%\bin\pg_ctl -D %CD%/data -l logfile start
ECHO "������� Enter ����� ���������� ������ �������"
pause
%CD%\bin\pg_ctl -D %CD%/data stop
