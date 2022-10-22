import speedtest
from tabulate import tabulate

st=speedtest.Speedtest()

class Network(object):
    def __init__(self):
        self.parser = speedtest.Speedtest()

    def data(self):
        down = str(f"{round(self.parser.download() / 1_000_000 , 2)} Mbps")
        up = str(f"{round(self.parser.upload() / 1_000_000, 2)} Mbps")
        servernames =[]   
        st.get_servers(servernames)   
        png=st.results.ping

        return [["Interface" , "Download", "Upload","Ping"],["JioFi2_06CE6B",down,up,png]]



    def __repr__(self):
        speed = self.data()
        return tabulate(speed, headers="firstrow", tablefmt="fancy_grid")

if __name__ == "__main__":
    print("Your Networ Speed Is : ")
    print(Network())
