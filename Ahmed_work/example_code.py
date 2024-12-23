import re

# Sample text
text = """
1996 Gulfstream G-IVSP 1289 N920KM for Sale: Specs, Price | ASO.com
Login
September 30, 02:56 AM US EDT
Welcome Guest
Login
/
Register
Logout
Buy
Sell
Learn
MyASO
You currently have JavaScript disabled on your browser. Please use the links below
to browse ASO.com
Buy
Find an Aircraft Dealer
Sell
Other
Single Engine Prop
US Dealers / Brokers
Broker / Dealer Rates
Industry Links and Services
Multi Engine Prop
International Dealers / Brokers
For Sale By Owner Rates
Business Jet
Alphabetical list of Dealers / Brokers
Business Turbo Prop
Turbine Helicopter
Piston Helicopter
Amphibian & Float
LSA & Experimental
Warbirds & Classic
Commercial Jet/TProp
Partnership Listings
Advanced
Search
Search
Please
log in
to access your Saved Searches.
There are no Saved Searches yet for this user account.
Learn About Fraud
Recently Viewed Aircraft
Manage My A/C Search
You are not experiencing the full functionality of ASO due to a particular
setting in your browser. Click here to learn how to fix this issue.
Listings Powered By:
Showing Listing
1
of
1
Previous
Next
Back to Search Results
Ad Reviewing Tools
Tag as Fav. & View in My A/C Search
Tag as Favorite
Tag as Viewed
Tag not interested
Create Notes
Report This Ad
Print Ad
Loan Calculator
Calculated Loan Payments:
Periodic Payments:
Total of all Payments:
Total Interest:
1996 Gulfstream G-IVSP
Reg # N920KM
Serial # 1289
Price: Inquire
TTAF: 6,513 Hrs.
Location: TN, US
Exterior
Interior
Interior
Interior
Interior
Interior
Interior
Interior
Interior
Panel
Zoom In
Zoom Out
Fit
We spent $500,000+ on new interior soft goods.
Airframe & Power Systems Information
Airframe
Landings: 3,979
Engines
Loc.
Make
Model
Serial#
TSN
CSN
TSML
L
Rolls Royce
TAY 611-8
16691
6486
3959
3472
R
16692
6513
3979
3472
L&R Engines Midlife c/w March 2006, Ice Tray SB c/w @ Midlife.
APU
Garrett GTCP-36-150 (G), Serial Number: P581C, TSN: 4,747, TSOH: 1,583
Maintenance Condition
Basic Operating Weight: 43,218 lbs.
Empty Weight: 41,967
Aircraft Maintenance Tracking Vehicle: CMP.net
Aircraft Maintenance Inspections Completed in Accordance with FAR 91.409 (f)3
36/72 Month Inspection(s) complied with April 2014 at Stevens (GYH)
48 Month Inspection complied with January 2012 by Jet Aviation, St. Louis
24 Month Inspection complied with July 2015 by Private Sky Aviation (RSW)
144 Month Inspection complied with March 2008 at GAC, Appleton
Avionics
Honeywell DU-880 6-tube EFIS
Honeywell TCZ-910 TCAS II w/ Chg 7
Fairchild F1000 FDR
Dual Honeywell Laser Ref II
Fairchild A100A CVR
Single Honeywell AHRS unit
Honeywell Primus WU-880 Color Radar
Artex C-406-2 / 110-406 ELT
Honeywell Mark V EGPWS w/ Visual Display
Dual Honeywell GPS
Dual CollinsTDR-94D / Mode S Transponders w/ Enhanced Flight ID (8 DAP) Capable
Dual Honeywell NZ 2000 w/ 6.0 Software Upgrade
Dual Collins VHF-422B Comms w/ 8.33 MHz Spacing
Dual Honeywell CDU 820 w/ Weather Graphics Available
Dual Collins VIR-432 VHF Navs w/ FM Immunity
Magnavox / Magnastar C2000 Flight phone with Aero H Satcom
Dual Collins RTU-4220 Radio Tuning Units
Dual Honeywell AA-300 Radar Altimeters
Honeywell SPZ-8400 Autopilot
Dual Collins ADF-462 ADF
DL-950 Data Loader
Dual Collins DME-442
Global Wulfsberg AFIS - DMU Upgrade to Support Graphic Weather
Dual Collins HF-9000 HF Comm w/ Selcal
Additional Features
RVSM Capable
8.33 KHz Spacing Compliant
FM Immunity Compliant
RNP Capable
MNPS Capable
Dual Electronic Flight Bags (CMC 1100)
BF Goodrich WX-1000 StormScope
Rosen Cockpit Sunvisor System
Thrust Reversers
Airshow 400
Davtron Clocks
Cabin Monitors Fwd / Aft
CD / DVD Player
FAX Machine
Precise Flight Pulselight System
Aft Baggage Net Modification
Interior
Refurbished 2015. 14 Place Interior plus Jump seats Fwd & Aft. Aft Lav. Magnastar Phone System w/Fax. Aero H SATCOM, Entertainment System. Interior Veneer, All Soft Goods except Headliner and Carpet Replaced August 2015 at Private Sky Aviation. Divans re-covered 2011. Aft Galley with Microwave, Dual Coffee Makers, Large Ice Drawer, High Temp Oven.
Exterior
Matterhorn White w/ Black and Red Stripes.
Contact Information
Please tell the seller that you saw this ad on ASO
Tel: (615) 361-3781
Fax: (615) 367-1226
404 BNA Dr.
Bldg. 200, Suite 305
Nashville, Tennessee 37217
All Specifications Subject to Verification Upon Inspection
Availability Subject to Prior Lease, Sale, or Withdrawal From Market Without Notice
Tag as Fav. &
View in My A/C Search
Tag as Favorite
Tag as Viewed
Tag not interested
Create Notes
Print ad
Loan calculator
ASO BuyerResponse
SM
System
Message to seller of
1996 Gulfstream G-IVSP
Serial:
#1289
Reg:
#N920KM
Price:
$
Name :
*
Company Name :
Phone :
Your E-Mail Address :
*
Country :
United States
Afghanistan
Aland Islands
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antarctica
Antigua And Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bosnia And Herzegovina
Botswana
Bouvet Is.
Brazil
British Indian Ocean Terr
Brunei Darussalam
Bulgaria
Burkina Faso
Burundi
Cambodia
Cameroon
Canada
Cape Verde
Cayman Is.
Central African Rep.
Chad
Chile
China
Christmas Is.
Cocos (Keeling) Is.
Colombia
Comoros
Congo
Congo Democratic Republic
Cook Is.
Costa Rica
Cote d'Ivoire
Croatia (Hrvatska)
Cuba
Curacao
Cyprus
Czech Republic
Denmark
Djibouti
Dominica
Dominican Republic
East Timor
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Falkland Is.(Malvinas)
Faroe Is.
Fiji
Finland
France
French Guiana
French Polynesia
French Southern Terr.
Gabon
Gambia
Georgia
Germany
Ghana
Gibraltar
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Heard And McDonald Is.
Holy See (Vatican City)
Honduras
Hong Kong
Hungary
Iceland
India
Indonesia
Iran, Islamic Rep. of
Iraq
Ireland
Isle of Man
Israel
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Korea, Dem People's Rep.
Korea, Republic of
Kuwait
Kyrgyzstan
Lao People's Dem Rep.
Latvia
Lebanon
Lesotho
Liberia
Libyan Arab Jamahiriya
Liechtenstein
Lithuania
Luxembourg
Macau
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Is.
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia, Federated States
Moldova, Republic of
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
Netherlands Antilles
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Is.
Northern Mariana Is.
Norway
Oman
Pakistan
Palau
Palestinian Territory
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Pitcairn
Poland
Portugal
Puerto Rico
Qatar
Reunion
Romania
Russian Federation
Rwanda
S. Georgia, Sandwich Is.
Saint Barthelemy
Saint Martin (French part)
Samoa
San Marino
Sao Tome And Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Maarten (Dutch part)
Slovakia (Slovak Rep.)
Slovenia
Solomon Is.
Somalia
South Africa
Spain
Sri Lanka
St. Helena
St. Kitts And Nevis
St. Lucia
St. Pierre & Miquelon
St. Vincent and Grenadines
Sudan
Suriname
Svalbard, Jan Mayen Is.
Swaziland
Sweden
Switzerland
Syrian Arab Republic
Taiwan
Tajikistan
Tanzania, United Rep. Of
Thailand
Timor-Leste
Togo
Tokelau
Tonga
Trinidad And Tobago
Tunisia
Turkey
Turkmenistan
Turks And Caicos Is.
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
United States Minor Is.
Uruguay
Uzbekistan
Vanuatu
Venezuela
Viet Nam
Virgin Is. (British)
Virgin Is. (U.S.)
Wallis And Futuna Is.
Western Sahara
Yemen
Yugoslavia
Zaire
Zambia
Zimbabwe
*
Message :
*
Forward a copy of this message to :
Me (email address entered above)
Additional email recipients
Enter Additional email
addresses separated by commas :
For security purposes, please
enter the characters shown below :
*
What's this?
* Required Item
By using this service, you accept our
Terms of Use
ASO Privacy Policy
Email to a Friend
Your E-mail Address :
*
Your First & Last Name :
*
Recipient's E-mail Address :
*
E-mail Subject :
From [Your Name]: 1996 Gulfstream G-IVSP for sale on ASO.com
E-mail Body :
[Your Name]
wanted you to see this 1996 Gulfstream G-IVSP that is currently for sale on ASO.com. To view the aircraft spec, including all available photos, please click on this link:
http://www.aso.com/listings/spec/ViewAd.aspx?id=136693
Personalized Message :
(300 characters max)
Enter the characters as shown below :
*
Security graphic :
What's this?
By using this service, you accept our
Terms of Use
ASO Privacy Policy
Report This Ad
I Would like to report this ad as inappropriate, suspicious or fraudulent.
*
Required fields. We will investigate this ad and use your contact details to report back to you.
Your E-mail Address :
*
Your First & Last Name :
*
E-mail Subject :
Report Ad: Ad # 136693 1996 Gulfstream G-IVSP
Describe why you are reporting this ad
(300 characters limit):
Enter the characters as shown below :
*
Security graphic :
What's this?
By using this service, you accept our
Terms of Use
Learn About Fraud
What's this?
To help prevent abuse of the ASO website, we require users to enter the 4 dynamic
characters displayed on the response form before submitting a message. This simple
measure greatly reduces the ability of automated programs to enable abuse of the
ASO website. While we cannot prevent all abuse, we constantly strive to ensure that
the ASO is as valuable as possible to our customers.
MyASO Aircraft Ad Notes
1996 Gulfstream G-IVSP
Reg #
N920KM
Target Price
General
Pros
Cons
All your notes are available each time you log in and
in your Manage My Aircraft Search page
Back
Loan Calculator
Purchase Price
Reset
No. of Payments
Down Payment
Settings
Periodic Payment
Loan Amount
Total of all Payments
Interest Rate (%)
Total Interest
Loan Calculator Settings
Purchase Price
Use asking price when available. If not available use user's target price.
Use target price when available. If not available use user's asking price.
Down Payment:
(enter % or $ amount)
Interest Rate:
%
No. of Payments:
What's this?
To help prevent abuse of the ASO BuyerResponse
SM
system, we require users
to enter the 4 dynamic characters displayed on the response form before submitting
a message. This simple measure greatly reduces the ability of automated programs
to enable abuse of the ASO website. While we cannot prevent all abuse, we constantly
strive to ensure that the BuyerResponse
SM
system is as valuable as possible
to our customers.
To help prevent abuse of the ASO website, we require users to enter the 4 dynamic
characters displayed on the response form before submitting a message. This simple
measure greatly reduces the ability of automated programs to enable abuse of the
ASO website. While we cannot prevent all abuse, we constantly strive to ensure that
the ASO is as valuable as possible to our customers.
Note: You must be logged in to your MyASO account to use Manage My Aircraft Search (
Free Registration
)
You are not experiencing the full functionality of ASO due to a particular
setting in your browser. Click here to learn how to fix this issue.
Login/Register
You have requested a feature that requires you to be logged in to your MyASO Account.
I have an existing MyASO account
I do not have a MyASO account
Login ID (email address)
Password
Email :
*
Confirm Email :
*
First Name :
*
Last Name :
*
Password :
*
Confirm Password :
*
Receive ASO Newsletter and Updates
Receive Weekly Latest Aircraft Listings Update
Receive ASO Notes (monthly market info publication)
Receive Periodic News/Updates from ASO
Note: At ASO, we hate SPAM as much as you do. We will never share your information
with any 3
rd
party, and we will always adhere to your wishes regarding
the types of email you wish you receive from us.
* Fields are Mandatory
Forgot my Password
Learn about the benefits of MyASO
Privacy Policy
Forgot Password
Please enter valid email address
Enter the email address of your MyASO Account:
Note: If you forgot your email address of your MyASO account, please
contact ASO Customer Service:
Mon-Fri
8:00am - 6:00pm ET
US Tel:
888-992-9276
Int'l Tel:
732-704-9561
Service:
service@aso.com
Forgot Password Email Link Confirmation
A link to the password reset form has been sent to
.
Please open this email, click on the link and follow instructions
to reset your password.
If you do not receive this email, please check your junk email folder and/or add accounts@aso.com to your safe senders list.
Privacy Policy
|
Terms of Use
|
Press Center
|
Site Map
Aircraft Shopper
Online, ASO, The ASO Logo, and The Aircraft Market in Real Time are registered United
States Trademarks
"""

# Function to extract information
def extract_aircraft_info(text):
    # Define regex patterns for each piece of information
    patterns = {
        'Date of Advertisement': r'date of advertisement\s*([\d/]+)',  # Extracts date in dd/mm/yyyy format
        'Manufacturer': r'mfr\s*([A-Za-z]+)',  # Extracts manufacturer (letters only)
        'Model': r'model\s*([A-Za-z0-9]+)',  # Extracts model (alphanumeric)
        'Registration Number': r'registration number\s*([A-Za-z0-9]+)',  # Extracts registration number (alphanumeric)
        'Year of Manufacture': r'year of manufacture\s*([\d.]+)',  # Extracts year (number with decimal)
        'Price': r'price\s*(\d+)',  # Extracts price (digits only)
        'Total Time Airframe (TTAF)': r'ttaf \(Total Time Airframe\)\s*(\d+)',  # Extracts TTAF (digits only)
        'Year Last Painted': r'Year Last Painted:\s*(\d{4})',  # Extracts year (4-digit year)
        'Year Last Interior Refurb': r'Year Last Interior Refurb:\s*(\d{4})',  # Extracts year (4-digit year)
    }

    # Dictionary to store the extracted information
    extracted_data = {}

    # Loop through patterns and extract information
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted_data[key] = match.group(1)
        else:
            extracted_data[key] = "Not Found"

    return extracted_data

# Call the function to extract information
aircraft_info = extract_aircraft_info(text)

# Print the extracted data in a user-friendly format
print("Extracted Aircraft Information:")
print("-" * 30)
for key, value in aircraft_info.items():
    print(f"{key}: {value}")
