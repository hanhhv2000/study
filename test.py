import sys
from streamlit import cli as stcli


if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "p1.py"]
    sys.exit(stcli.main())
