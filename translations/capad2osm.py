
import re
import string

def translateOperator(code):
    authorityLookup = {
        'AAD': 'Australian Antarctic Division',
        'AC_SA': 'Alexandrina Council',
        'ACT_TAMSD': 'ACT Territory and Municipal Services Directorate',
        'AWC': 'Australian Wildlife Conservancy',
        'AWC & BA': 'Australian Wildlife Conservancy & Birds Australia',
        'BBT': 'Bookmark Biosphere Trust',
        'BHA': 'Bush Heritage Australia',
        'CCC_QLD': 'Caloundra City Council',
        'CR PTY LTD': 'Conservation Reserves PTY LTD',
        'DOE': 'Australian Government, Department of the Environment',
        'EAC_QLD': 'Ewamian Aboriginal Corporation',
        'EL Inc._NSW': 'Enduring Landscapes Inc.',
        'FC_NSW': 'Forestry Commission of NSW',
        'FPR Inc.': 'Friends of the Porongurup Range (Inc)',
        'GCC_NSW': 'Gosford City Council',
        'HCR_CMA': 'Hunter - Central Rivers Catchment Management Authority',
        'ILC_NT': 'Indigenous Land Corporation',
        'IMG': 'Indigenous management group',
        'IMG, LILC': 'Indigenous management group and Local Indigenous Land Council',
        'KRGC_NSW': 'Ku-ring-gai Council',
        'LHI_Board': 'Lord Howe Island Board',
        'LILC': 'Local Indigenous Land Council',
        'LVRC_Q_EPA': 'Lockyer Valley Regional Council and QLD EPA',
        'MINCA_QLD': 'Magnetic Island Nature Care Association',
        'NF SA Inc.': 'Nature Foundation SA Inc',
        'NSC_QLD': 'Noosa Shire Council',
        'NSW_OEH': 'NSW Office of Environment and Heritage',
        'NT_PWCNT': 'Parks and Wildlife Commission of the NT',
        'QLD_DERM': 'Queensland Department of Environment and Resource Management',
        'QLD_EHP': 'Queensland Department of Environment and Heritage Protection',
        'QLD_EPA': 'Queensland Environment Protection Agency',
        'QLD_NPRSR': 'Queensland Department of National Parks, Recreation, Sport and Racing',
        'SA_DEH': 'South Australian Department of Environment and Heritage',
        'SA_DEWNR': 'South Australian Department of Environment, Water and Natural Resources',
        'F_SA': 'Forestry South Australia',
        'SCRC_QLD': 'Sunshine Coast Regional Council',
        'TAS_DPIPWE': 'Tasmanian Department of Primary Industries, Parks, Water and Environment',
        'TAS_WPMT': 'Wellington Park Management Trust Tasmania',
        'TFN_VIC': 'Trust for Nature (Victoria)',
        'TLC Inc_TAS': 'Tasmanian Land Conservancy Inc.',
        'TSRA': 'Torres Strait Regional Authority',
        'TTTN': 'The Trustee for the Trust for Nature',
        'U. Ballarat': 'University of Ballarat',
        'VIC_DEPI': 'Victorian Department of Environment and Primary Industries',
        'WA_DPAW': 'Western Australian Department of Parks and Wildlife',
        'WAC': 'Winangakirri Aboriginal Corporation',
        'WEC': 'Worlds End Conservation Pty Ltd'
        }
    return authorityLookup.get(code)

def translateAttribution(code):
    datasourceLookup = {
        'AAD': 'Australian Antarctic Division',
        'ACT_TAMSD': 'ACT Territory and Municipal Services Directorate',
        'DOE': 'Australian Government, Department of the Environment',
        'DOE_NRSP': 'Australian Government, Department of the Environment - National Reserve System Program',
        'F_SA': 'Forestry South Australia',
        'FC_NSW': 'Forestry Commission of NSW',
        'LHI_Board': 'Lord Howe Island Board',
        'NSW_OEH': 'NSW Office of Environment and Heritage',
        'NT_PWCNT': 'Parks and Wildlife Commission of the NT',
        'QLD_EHP': 'Queensland Department of Environment and Heritage Protection',
        'QLD_NPRSR': 'Queensland Department of National Parks, Recreation, Sport and Racing',
        'SA_DEWNR': 'South Australian Department of Environment, Water and Natural Resources',
        'TAS_DPIPWE': 'Tasmanian Department of Primary Industries, Parks, Water and Environment',
        'VIC_DEPI': 'Victorian Department of Environment and Primary Industries',
        'WA_DPAW': 'Western Australian Department of Parks and Wildlife'
        }
    return datasourceLookup.get(code)

def translateProtectClass(code):
    protectClassLookup = {
        'AA':'21',
        'ACCP':'',
        'ASMA':'',
        'ASPA':'',
        'BG':'4',
        'CA':'',
        'CCA':'',
        'CCAZ1':'',
        'CCAZ3':'',
        'COR':'',
        'CP':'4',
        'CR':'',
        'FLR':'4',
        'FR':'4',
        'GR':'4',
        'HA':'22',
        'HIR':'22',
        'HPOT':'4',
        'HR':'2',
        'HS':'22',
        'HTR':'',
        'IPA':'',
        'KCR':'3',
        'MA':'',
        'MAA':'3',
        'MCP':'',
        'MNP':'2',
        'MR':'',
        'MS':'14',
        'NAP':'4',
        'NCA':'1',
        'NCR':'',
        'NFR':'4',
        'NP':'2',
        'NPA':'',
        'NPC':'',
        'NR':'1',
        'NRA':'',
        'NREF':'4',
        'NRS':'',
        'OCA':'5',
        'OCA/NAP':'5',
        'OP':'',
        'PA':'',
        'PNPA':'',
        'PNR':'',
        'PPP':'',
        'PS':'',
        'RA':'1',
        'REP':'',
        'RNA':'1',
        'RP':'',
        'RR':'4',
        'S5G':'',
        'S5H':'',
        'SCA':'',
        'SP':'1b',
        'SR':'2',
        'WPA':'1b',
        'WP':'1b',
        'WZ':'1b'
        }

    return protectClassLookup.get(code)

def translateGovernanceType(code):
    lookup = {
            'G': 'government_managed ',
            'C': 'social_group',
            'J': 'joint', # joint with who?
            'P': 'private_landowner'

            }
    return lookup.get(code)

def formatDate(date):
    return string.replace(date, '/', '-')


def filterTags(attrs):
    if not attrs: return

    tags = {}

    #Add the source and attribution
    tags.update({
        'source':'Collaborative Australian Protected Areas Database (CAPAD) 2014, Commonwealth of Australia 2014'
        })

    tags.update({'boundary':'protected_area'})

    # name (if not unnamed)
    if attrs['NAME']:
        if (re.match('Unnamed', attrs['NAME']) is None):
            tags.update({'name': attrs['NAME'] + ' ' + attrs['TYPE']})

    # protection_title from TYPE
    if attrs['TYPE']:
        tags.update({'protection_title':attrs['TYPE']})

    # protect_class derived from TYPE_ABBR
    if attrs['TYPE_ABBR']:
        tags.update({'protect_class': translateProtectClass(attrs['TYPE_ABBR'])})

    # start_date
    if attrs['GAZ_DATE']:
        tags.update({'start_date': formatDate(attrs['GAZ_DATE'])})

    # operator
    if attrs['AUTHORITY']:
        tags.update({'operator': translateOperator(attrs['AUTHORITY'])})

    # attribution
    if attrs['DATASOURCE']:
        tags.update({'attribution': translateAttribution(attrs['DATASOURCE'])})

    # governance_type
    if attrs['GOVERNANCE']:
        tags.update({'governance_type': translateGovernanceType(attrs['GOVERNANCE'])})

    # ref
    if attrs['PA_ID']:
        tags.update({'ref': attrs['PA_ID']})

    return tags
