# Wake-On-LAN

import xbmcaddon, sys, time

# Read Settings
settings = xbmcaddon.Addon( id="script.advanced.wol" )
autostart = settings.getSetting("autostart")
wolAfterStandby = settings.getSetting("wolAfterStandby")

if (autostart == "true"):
  import default
  default.main(True)
  if (wolAfterStandby == "true"):
	print "script.advanced.wol: Waiting for resume from standby"
	previousTime = time.time()
	while (not xbmc.abortRequested):
		if ( time.time()-previousTime > 5):
			print "script.advanced.wol: Start WOL script after return from standby"
			default.main(True)
			previousTime = time.time()
			xbmc.sleep(1000)
		else:
			previousTime = time.time()
			xbmc.sleep(1000)