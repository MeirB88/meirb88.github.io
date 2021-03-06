# coding= utf-8
import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR royalblue]MEIR[/COLOR] [COLOR gold]WIZARD[/COLOR]'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'https://meir1998.000webhostapp.com/wizard/builds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/buildsicon.png'
ICONMAINT      = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/mainticon.png'
ICONAPK        = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/apkicon.png'
ICONADDONS     = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/ADDONSICON.png'
ICONYOUTUBE    = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/youtubeicon.png'
ICONSAVE       = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/dataicon.png'
ICONTRAKT      = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/TRAKTICON.png'
ICONREAL       = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/dataicon.png'
ICONLOGIN      = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/loginicon.png'
ICONCONTACT    = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/CONTACTICON.png'
ICONSETTINGS   = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/SETTINGSICON.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '[COLOR royalblue]----------------------------------[/COLOR]'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'royalblue'
COLOR2         = 'gold'
COLOR3         = 'white'
COLOR3         = 'teal'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']%s[/COLOR] [COLOR '+COLOR2+']בילד נוכחי:[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = ''
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.meirwizard'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/MeirB88/meirb88.github.io/master/zips/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/MeirB88/meirb88.github.io/master/zips'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = ''
NOTIFICATION2  = ''
NOTIFICATION3  = ''
NOTIFICATION4  = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = '[B]Meir Wizard[/B]'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'https://meir1998.000webhostapp.com/wizard/Wizard%20Icons/fanart.png'
#########################################################