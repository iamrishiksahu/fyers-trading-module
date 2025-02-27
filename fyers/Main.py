from .HistoricalDataDownloader import HistoricalDataDownloader
from .Broker import Broker 
from .LiveMarketFeed import LiveMarketFeed
import time

class Main:
    
    def __init__(self):
        pass
            
        
    
    def run(self):
        
        broker = Broker()
        if broker is None:
            print("Oops, broker could not be initialized")
            return
    
        # Sample implementation of downloading historical data for NIFTY 50
        hdl = HistoricalDataDownloader(broker)
        hdl.setScripts([
            # "NSE:NIFTY50-INDEX",
            "NSE:NIFTY2512323000CE",
            # f"{'NSE'}:{'NIFTY'}{'24'}{'4'}{'18'}{'22600'}{'CE'}"
        ])
        
        startDate = "2024-03-15"
        endDate = "2025-03-20"
        timeframe = "5S"
        hdl.downloadData(startDate, endDate, timeframe)
        
        # You can write your own implementation here
        
        
        # lmf = LiveMarketFeed()
        # lmf.setFeedHandler(self.feedHandler)
        # lmf.setSubscriptionScripts(["NSE:ADANIPORTS-EQ"])
        # lmf.setForwardSocketUrl("http://localhost:8088")
        
        # lmf.start()
        
        # time.sleep(10)        
        
        # lmf.addSubscriptionScripts(["NSE:GRASIM-EQ"])
        
        
    def feedHandler(self, feed):
        print("FEED",feed)
        
