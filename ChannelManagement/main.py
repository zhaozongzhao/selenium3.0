import pytest

# {
# 	"cmd": ["/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6", "-u", "$file"],
#       "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
#       "selector": "source.python"
# }
if __name__ == '__main__':
    pytest.main(["-m order","--html=HtmlReport/smoke_report.html"])
