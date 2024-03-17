@echo off
python -m pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser firefox

REM pytest -v -s -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
REM pytest -v -s -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome
REM pytest -v -s -m "regression" --html=Reports/report.html testCases/ --browser chrome