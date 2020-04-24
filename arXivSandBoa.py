import urllib.request
import feedparser
import os
import progressbar
import time


#arXiv Sand boa v.0
#Created by P.D.M.Dilan
#2020/04/22

#Subject Classification list
SubCalf=[('Astrophysics', 'astro-ph'), ('Cosmology and Nongalactic Astrophysics', 'astro-ph.CO'), ('Earth and Planetary Astrophysics', 'astro-ph.EP'), ('Astrophysics of Galaxies', 'astro-ph.GA'), ('High Energy Astrophysical Phenomena', 'astro-ph.HE'), ('Instrumentation and Methods for Astrophysics', 'astro-ph.IM'), ('Solar and Stellar Astrophysics', 'astro-ph.SR'), ('Disordered Systems and Neural Networks', 'cond-mat.dis-nn'), ('Mesoscale and Nanoscale Physics', 'cond-mat.mes-hall'), ('Materials Science', 'cond-mat.mtrl-sci'), ('Other Condensed Matter', 'cond-mat.other'), ('Quantum Gases', 'cond-mat.quant-gas'), ('Soft Condensed Matter', 'cond-mat.soft'), ('Statistical Mechanics', 'cond-mat.stat-mech'), ('Strongly Correlated Electrons', 'cond-mat.str-el'), ('Superconductivity', 'cond-mat.supr-con'), ('Artificial Intelligence', 'cs.AI'), ('Hardware Architecture', 'cs.AR'), ('Computational Complexity', 'cs.CC'), ('Computational Engineering, Finance, and Science', 'cs.CE'), ('Computational Geometry', 'cs.CG'), ('Computation and Language', 'cs.CL'), ('Cryptography and Security', 'cs.CR'), ('Computer Vision and Pattern Recognition', 'cs.CV'), ('Computers and Society', 'cs.CY'), ('Databases', 'cs.DB'), ('Distributed, Parallel, and Cluster Computing', 'cs.DC'), ('Digital Libraries', 'cs.DL'), ('Discrete Mathematics', 'cs.DM'), ('Data Structures and Algorithms', 'cs.DS'), ('Emerging Technologies', 'cs.ET'), ('Formal Languages and Automata Theory', 'cs.FL'), ('General Literature', 'cs.GL'), ('Graphics', 'cs.GR'), ('Computer Science and Game Theory', 'cs.GT'), ('Human-Computer Interaction', 'cs.HC'), ('Information Retrieval', 'cs.IR'), ('Information Theory', 'cs.IT'), ('Learning', 'cs.LG'), ('Logic in Computer Science', 'cs.LO'), ('Multiagent Systems', 'cs.MA'), ('Multimedia', 'cs.MM'), ('Mathematical Software', 'cs.MS'), ('Numerical Analysis', 'cs.NA'), ('Neural and Evolutionary Computing', 'cs.NE'), ('Networking and Internet Architecture', 'cs.NI'), ('Other Computer Science', 'cs.OH'), ('Operating Systems', 'cs.OS'), ('Performance', 'cs.PF'), ('Programming Languages', 'cs.PL'), ('Robotics', 'cs.RO'), ('Symbolic Computation', 'cs.SC'), ('Sound', 'cs.SD'), ('Software Engineering', 'cs.SE'), ('Social and Information Networks', 'cs.SI'), ('Systems and Control', 'cs.SY'), ('Econometrics', 'econ.EM'), ('Audio and Speech Processing', 'eess.AS'), ('Image and Video Processing', 'eess.IV'), ('Signal Processing', 'eess.SP'), ('General Relativity and Quantum Cosmology', 'gr-qc'), ('High Energy Physics - Experiment', 'hep-ex'), ('High Energy Physics - Lattice', 'hep-lat'), ('High Energy Physics - Phenomenology', 'hep-ph'), ('High Energy Physics - Theory', 'hep-th'), ('Commutative Algebra', 'math.AC'), ('Algebraic Geometry', 'math.AG'), ('Analysis of PDEs', 'math.AP'), ('Algebraic Topology', 'math.AT'), ('Classical Analysis and ODEs', 'math.CA'), ('Combinatorics', 'math.CO'), ('Category Theory', 'math.CT'), ('Complex Variables', 'math.CV'), ('Differential Geometry', 'math.DG'), ('Dynamical Systems', 'math.DS'), ('Functional Analysis', 'math.FA'), ('General Mathematics', 'math.GM'), ('General Topology', 'math.GN'), ('Group Theory', 'math.GR'), ('Geometric Topology', 'math.GT'), ('History and Overview', 'math.HO'), ('Information Theory', 'math.IT'), ('K-Theory and Homology', 'math.KT'), ('Logic', 'math.LO'), ('Metric Geometry', 'math.MG'), ('Mathematical Physics', 'math.MP'), ('Numerical Analysis', 'math.NA'), ('Number Theory', 'math.NT'), ('Operator Algebras', 'math.OA'), ('Optimization and Control', 'math.OC'), ('Probability', 'math.PR'), ('Quantum Algebra', 'math.QA'), ('Rings and Algebras', 'math.RA'), ('Representation Theory', 'math.RT'), ('Symplectic Geometry', 'math.SG'), ('Spectral Theory', 'math.SP'), ('Statistics Theory', 'math.ST'), ('Mathematical Physics', 'math-ph'), ('Adaptation and Self-Organizing Systems', 'nlin.AO'), ('Chaotic Dynamics', 'nlin.CD'), ('Cellular Automata and Lattice Gases', 'nlin.CG'), ('Pattern Formation and Solitons', 'nlin.PS'), ('Exactly Solvable and Integrable Systems', 'nlin.SI'), ('Nuclear Experiment', 'nucl-ex'), ('Nuclear Theory', 'nucl-th'), ('Accelerator Physics', 'physics.acc-ph'), ('Atmospheric and Oceanic Physics', 'physics.ao-ph'), ('Applied Physics', 'physics.app-ph'), ('Atomic and Molecular Clusters', 'physics.atm-clus'), ('Atomic Physics', 'physics.atom-ph'), ('Biological Physics', 'physics.bio-ph'), ('Chemical Physics', 'physics.chem-ph'), ('Classical Physics', 'physics.class-ph'), ('Computational Physics', 'physics.comp-ph'), ('Data Analysis, Statistics and Probability', 'physics.data-an'), ('Physics Education', 'physics.ed-ph'), ('Fluid Dynamics', 'physics.flu-dyn'), ('General Physics', 'physics.gen-ph'), ('Geophysics', 'physics.geo-ph'), ('History and Philosophy of Physics', 'physics.hist-ph'), ('Instrumentation and Detectors', 'physics.ins-det'), ('Medical Physics', 'physics.med-ph'), ('Optics', 'physics.optics'), ('Plasma Physics', 'physics.plasm-ph'), ('Popular Physics', 'physics.pop-ph'), ('Physics and Society', 'physics.soc-ph'), ('Space Physics', 'physics.space-ph'), ('Biomolecules', 'q-bio.BM'), ('Cell Behavior', 'q-bio.CB'), ('Genomics', 'q-bio.GN'), ('Molecular Networks', 'q-bio.MN'), ('Neurons and Cognition', 'q-bio.NC'), ('Other Quantitative Biology', 'q-bio.OT'), ('Populations and Evolution', 'q-bio.PE'), ('Quantitative Methods', 'q-bio.QM'), ('Subcellular Processes', 'q-bio.SC'), ('Tissues and Organs', 'q-bio.TO'), ('Computational Finance', 'q-fin.CP'), ('Economics', 'q-fin.EC'), ('General Finance', 'q-fin.GN'), ('Mathematical Finance', 'q-fin.MF'), ('Portfolio Management', 'q-fin.PM'), ('Pricing of Securities', 'q-fin.PR'), ('Risk Management', 'q-fin.RM'), ('Statistical Finance', 'q-fin.ST'), ('Trading and Market Microstructure', 'q-fin.TR'), ('Quantum Physics', 'quant-ph'), ('Applications', 'stat.AP'), ('Computation', 'stat.CO'), ('Methodology', 'stat.ME'), ('Machine Learning', 'stat.ML'), ('Other Statistics', 'stat.OT'), ('Statistics Theory', 'stat.TH')]

banner=(r"""

  .--.  ,---.  .-.   .-.,-..-.   .-.    .---.  .--.  .-. .-. ,'|"\     ,---.    .---.    .--.  
 / /\ \ | .-.\  ) \_/ / |(| \ \ / /    ( .-._)/ /\ \ |  \| | | |\ \    | .-.\  / .-. )  / /\ \ 
/ /__\ \| `-'/ (_)   /  (_)  \ V /    (_) \  / /__\ \|   | | | | \ \   | |-' \ | | |(_)/ /__\ \
|  __  ||   (    / _ \  | |   ) /     _  \ \ |  __  || |\  | | |  \ \  | |--. \| | | | |  __  |
| |  |)|| |\ \  / / ) \ | |  (_)     ( `-'  )| |  |)|| | |)| /(|`-' /  | |`-' /\ `-' / | |  |)|
|_|  (_)|_| \)\`-' (_)-'`-'           `----' |_|  (_)/(  (_)(__)`--'   /( `--'  )---'  |_|  (_)
            (__)                                    (__)              (__)     (_)             
                
                ~~ arXiv.org e-Print archive's research paper downloader ~~
                                ~~ arXiv sand boa version 0.0 ~~
                
                """)

print(banner)
print('\n')

print('------------------------------------  List of categories  ------------------------------------\n')

#Print subject list to select subject
i=1
for key,value in SubCalf:
    print(i,key)
    i=i+1

#------------------------------------------------------------------------------------------------------------------
#get user input
print('\n')
categoryVar2=input('Select a category number : ')

contains_digit = any(map(str.isdigit, categoryVar2))

#check input is a number or not
while not(contains_digit):
    print('Not a number !')
    categoryVar2=input('Select a category number : ')
    contains_digit = any(map(str.isdigit, categoryVar2))

categoryVar2=int(categoryVar2)

#validate the input with in the range
while not(categoryVar2 <154) or not(categoryVar2 > 0):
    print('Invaild number !')
    categoryVar2=input('Select a category number : ')
    categoryVar2=int(categoryVar2)


#get the default download path
#------------------------------------------------------------------------------------------------------------------
def get_download_path():
#"""Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
# progress bar
pbar = None

def show_progress(block_num, block_size, total_size):
    global pbar
    try:
        if pbar is None:
            Fsize=str(int(round(total_size/1024)))
            print('File size : '+ Fsize +' KB')
            widgets=[                   
                        progressbar.Percentage(),
                        progressbar.Bar(),                    
                        ' (', progressbar.Timer(), ') ',
                        ' (', progressbar.ETA(), ') ',
                    ]
            pbar = progressbar.ProgressBar(maxval=total_size, widgets=widgets)        
            pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            pbar.update(downloaded)
        else:
            pbar.finish()
            pbar = None
    except AttributeError:
        print('Something wrong with file :( ')
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------

# Downloding the research paper
def downloadResearchPapers():

    print('------------------------------------  Download Files  ------------------------------------\n')
    print('To download multiple papers once, use comma (,) and type next arxiv-id. Ex :16xx.xxx8v1,17xx.xxxx5v1,15xx.xxxx3v1\n')
    print('Type navig or enter default to navigate through papers again !\n')
    dLoadValList=input('Type arxiv-id to download the research paper (Default navig) : ') or 'navig'

    if dLoadValList == 'navig':
        navigateThroughSystem()
    else:
        dLoadValListClean = [x.strip() for x in dLoadValList.split(',') if x != '']

        #fetch download path
        downloadPath=get_download_path()

        lenthOfList=len(dLoadValListClean)
        counter=1

        for dLoadVal in dLoadValListClean:
            for entry in navigateThroughSystem.feed.entries:
                try:
                    if entry.id.split('/abs/')[-1] == dLoadVal :
                        for link in entry.links:
                            if link.rel == 'alternate':
                                print(' ')
                            elif link.title == 'pdf':               
                                print('Starting download now !')
                                #clean pdf name from sepcial characters
                                dLoadValCleaned = dLoadVal.translate({ord(c): None for c in '!@#$/\\'})                
                                urllib.request.urlretrieve(link.href, downloadPath+'\\'+dLoadValCleaned+'.pdf',show_progress)                
                                print('Download Completed !')

                except:
                    print('Something bad happend to this file !')
                    exit()
            if counter < lenthOfList:
                print('Ready to download next item !')
                counter=counter + 1
    exit()

#------------------------------------------------------------------------------------------------------------------

def navigateThroughSystem():
#------------------------------------------------------------------------------------------------------------------
# get user input as max result view

    print('\n')
    maxNumRes=input('Enter number of results to view (Default 10) : ') or '10'

    contains_digit = any(map(str.isdigit, maxNumRes))

#check input is a number or not
    while not(contains_digit):
        print('Not a number !')
        maxNumRes=input('Enter number of results to view (Default 10) : ') or '10'
        contains_digit = any(map(str.isdigit, maxNumRes))



#------------------------------------------------------------------------------------------------------------------
# get user input as starting point of results

    stPoint=input('Enter starting point for result view (Default 0) : ') or '0'

    contains_digit = any(map(str.isdigit, stPoint))

#check input is a number or not
    while not(contains_digit):
        print('Not a number !')
        stPoint=input('Enter starting point for result view (Default 0) : ') or '0'
        contains_digit = any(map(str.isdigit, stPoint))


#------------------------------------------------------------------------------------------------------------------
    print('\n')
    print('You have selected -----> '+ SubCalf[categoryVar2 -1 ][0] +' and '+ maxNumRes +' results will be shown !')
    print('\n')
    subjectForSearch=SubCalf[categoryVar2 -1 ][1]

    url = 'http://export.arxiv.org/api/query?search_query=all:%s&start=%s&max_results=%s' % (subjectForSearch,stPoint,maxNumRes)
    data = urllib.request.urlopen(url).read()


#------------------------ Below code segment has taken from arXiv Parsing Example----------------------------------------
#https://static.arxiv.org/static/arxiv.marxdown/0.1/help/api/examples/python_arXiv_parsing_example.txt

    navigateThroughSystem.feed = feedparser.parse(data)
    print('------------------------------------  Query Summary  ------------------------------------\n')
# print out feed information
    print('Feed last updated: %s' % navigateThroughSystem.feed.feed.updated)

# print opensearch metadata
    print('Total Results for this query: %s' % navigateThroughSystem.feed.feed.opensearch_totalresults)
    print('Items Per Page for this query: %s' % navigateThroughSystem.feed.feed.opensearch_itemsperpage)
    print('Start Index for this query: %s'   % navigateThroughSystem.feed.feed.opensearch_startindex)
    print('------------------------------------  *************  ------------------------------------\n')


# Run through each entry, and print out information
    for entry in navigateThroughSystem.feed.entries:

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Paper Detail   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print('arxiv-id: %s' % entry.id.split('/abs/')[-1])
        print('Published: %s' % entry.published)
        print('Title:  %s' % entry.title)
        # feedparser v4.1 only grabs the first author
        author_string = entry.author
    
        # grab the affiliation in <arxiv:affiliation> if present
        # - this will only grab the first affiliation encountered
        #   (the first affiliation for the first author)
        # Please email the list with a way to get all of this information!
        try:
            author_string += ' (%s)' % entry.arxiv_affiliation
        except AttributeError:
            pass
    
        print('Last Author:  %s' % author_string)
    
        # feedparser v5.0.1 correctly handles multiple authors, print them all
        try:
            print('Authors:  %s' % ', '.join(author.name for author in entry.authors))
        except AttributeError:
            pass

        # The journal reference, comments and primary_category sections live under 
        # the arxiv namespace
        try:
            journal_ref = entry.arxiv_journal_ref
        except AttributeError:
            journal_ref = 'No journal ref found'
        print('Journal reference: %s' % journal_ref)
    
        try:
            comment = entry.arxiv_comment
        except AttributeError:
            comment = 'No comment found'
        print('Comments: %s' % comment)

        # The abstract is in the <summary> element
        print('Abstract: %s' %  entry.summary)
        print('\n')
    downloadResearchPapers()

#------------------------------------------------------------------------------------------------------------------
#Call for run the sytem

navigateThroughSystem()
downloadResearchPapers()

#------------------------------------------------------------------------------------------------------------------
