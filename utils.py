import pygeoip

gi = pygeoip.GeoIP('/usr/local/share/GeoIP/GeoIP.dat', pygeoip.MEMORY_CACHE)

gametypes = {
	"sd": "Search & Destroy",
	"dm": "Deathmatch",
	"war": "Team Deathmatch",
	"dom": "Domination",
	"ctf": "Capture the Flag",
	"dd": "Demolition",
	"m40a3": "M40A3",
	"gg": "GunGame",
	"dmc": "Deathmatch Classic"
}

def gametype(s):
	try:
		return gametypes[s]
	except:
		return s

mapnames = {
	"mp_afghan": "Afghan",
	"mp_derail": "Derail",
	"mp_estate": "Estate",
	"mp_favela": "Favela",
	"mp_highrise": "Highrise",
	"mp_invasion": "Invasion",
	"mp_checkpoint": "Karachi",
	"mp_quarry": "Quarry",
	"mp_rundown": "Rundown",
	"mp_rust": "Rust",
	"mp_boneyard": "Scrapyard",
	"mp_nightshift": "Skidrow",
	"mp_subbase": "Sub Base",
	"mp_terminal": "Terminal",
	"mp_underpass": "Underpass",
	"mp_brecourt": "Wasteland",
	"mp_complex": "Bailout",
	"mp_crash": "Crash",
	"mp_compact": "Salvage",
	"mp_overgrown": "Overgrown",
	"mp_storm": "Storm",
	"mp_abandon": "Carnival",
	"mp_fuel2": "Fuel",
	"mp_strike": "Strike",
	"mp_trailerpark": "Trailer Park",
	"mp_vacant": "Vacant",
	"mp_nuked": "Nuketown",
	"oilrig": "Oilrig",
}

def mapname(s):
	try:
		return mapnames[s]
	except:
		return s

def trim(s):
	x = "".join(i for i in s if ord(i)<128)
	return x.strip()

def geoip(ip):
	ip = ip.split(":")[0]
	return gi.country_code_by_addr(ip)

def colour(s):
	s = s.replace('^0', '</span><span style="color: #000000">')
	s = s.replace('^1', '</span><span style="color: #ff0000">')
	s = s.replace('^2', '</span><span style="color: #00ff00">')
	s = s.replace('^3', '</span><span style="color: #ffff00">')
	s = s.replace('^4', '</span><span style="color: #0000ff">')
	s = s.replace('^5', '</span><span style="color: #00ffff">')
	s = s.replace('^6', '</span><span style="color: #ff00ff">')
	s = s.replace('^7', '</span><span style="color: #ffffff">')
	s = s.replace('^8', '</span><span style="color: #CC9933">')
	s = s.replace('^9', '</span><span style="color: #000000">')
	return '<span>' + s + '</span>'
