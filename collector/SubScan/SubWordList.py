import sys
sys.dont_write_bytecode=True

mydict=['11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '3', '3com', '4', '5', '6', '7', '8', '9', 'a','a.auth-ns','a01',
        'a02', 'a1', 'a2', 'abc', 'about','ac', 'academico', 'acceso', 'access', 'accounting', 'accounts', 'acid', 'activestat', 'ad',
        'adam', 'adkit', 'admin', 'administracion', 'administrador', 'administrator', 'administrators', 'admins', 'ads', 'adsense','adserver',
        'adsl', 'ae', 'af', 'affiliate', 'affiliates', 'affiliati', 'afiliados', 'ag', 'agenda', 'agent', 'ai', 'aix', 'ajax', 'ak',
        'akamai','al', 'alabama', 'alaska', 'albuquerque', 'alerts', 'alpha', 'alterwind', 'am', 'amarillo', 'americas', 'an', 'anaheim', 'analyzer', 'announce', 'announcements', 'antivirus', 'ao', 'ap', 'apache', 'apollo', 'app', 'app01', 'app1', 'apple',
        'application', 'applications', 'apps', 'appserver', 'aq', 'ar', 'archie', 'arcsight', 'argentina', 'arizona', 'arkansas',
        'arlington', 'as', 'as400', 'asia', 'asterix', 'at', 'athena', 'atlanta', 'atlas', 'att', 'au', 'auction', 'austin', 'auth', 'auto',
        'av', 'aw', 'ayuda', 'az', 'b', 'b.auth-ns', 'b01', 'b02', 'b1', 'b2', 'b2b', 'b2c', 'ba', 'back', 'backend', 'backup', 'baker',
        'bakersfield', 'balance', 'balancer', 'baltimore', 'banking', 'bayarea', 'bb', 'bbdd', 'bbs', 'bd', 'bdc', 'be', 'bea', 'beta', 'bf',
        'bg', 'bh', 'bi', 'billing', 'biz', 'biztalk', 'bj', 'black', 'blackberry', 'blog', 'blogs', 'blue', 'bm', 'bn', 'bnc', 'bo', 'bob',
        'bof', 'boise', 'bolsa', 'border', 'boston','boulder','boy','br','bravo','brazil','britian','broadcast','broker','bronze','brown',
        'bs', 'bsd', 'bsd0', 'bsd01', 'bsd02', 'bsd1', 'bsd2', 'bt', 'bug', 'buggalo', 'bugs', 'bugzilla', 'build', 'bulletins', 'burn',
        'burner', 'buscador', 'buy', 'bv', 'bw', 'by', 'bz', 'c', 'c.auth-ns', 'ca', 'cache', 'cafe', 'calendar', 'california', 'call',
        'calvin', 'canada', 'canal', 'canon', 'careers', 'catalog', 'cc', 'cd', 'cdburner', 'cdn', 'cert', 'certificates', 'certify',
        'certserv', 'certsrv', 'cf', 'cg', 'cgi', 'ch', 'channel', 'channels', 'charlie', 'charlotte', 'chat', 'chats', 'chatserver',
        'check', 'checkpoint', 'chi', 'chicago', 'ci', 'cims', 'cincinnati', 'cisco', 'citrix', 'ck', 'cl', 'class', 'classes',
        'classifieds', 'classroom', 'cleveland', 'clicktrack', 'client', 'clientes', 'clients', 'club', 'clubs', 'cluster', 'clusters',
        'cm', 'cmail', 'cms', 'cn', 'co', 'cocoa', 'code', 'coldfusion', 'colombus', 'colorado', 'columbus', 'com', 'comunicare',
        'comunicati', 'comunicazione', 'commerce', 'commerceserver', 'communigate', 'community', 'compaq', 'compras', 'con','concentrator', 'conf',
        'conference', 'conferencing', 'confidential', 'connect', 'connecticut', 'consola', 'console', 'consult', 'consultant','consultants','consulting',
        'consumer', 'contact', 'content', 'contracts', 'core', 'core0', 'core01', 'corp', 'corpmail', 'corporate', 'correo', 'correoweb',
        'cortafuegos', 'counterstrike', 'courses', 'cr', 'cricket', 'crm', 'crs', 'cs', 'cso', 'css', 'ct', 'cu', 'cust1', 'cust10','cust100','cust101','cust102',
        'cust103', 'cust104', 'cust105', 'cust106', 'cust107', 'cust108', 'cust109', 'cust11', 'cust110', 'cust111', 'cust112','cust113',
        'cust114', 'cust115', 'cust116', 'cust117', 'cust118', 'cust119', 'cust12', 'cust120', 'cust121', 'cust122', 'cust123','cust124',
        'cust125', 'cust126', 'cust13', 'cust14', 'cust15', 'cust16', 'cust17', 'cust18', 'cust19', 'cust2', 'cust20', 'cust21',
        'cust22', 'cust23', 'cust24', 'cust25', 'cust26', 'cust27', 'cust28', 'cust29', 'cust3', 'cust30', 'cust31', 'cust32', 'cust33',
        'cust34', 'cust35', 'cust36', 'cust37', 'cust38', 'cust39', 'cust4', 'cust40', 'cust41', 'cust42', 'cust43', 'cust44', 'cust45',
        'cust46', 'cust47', 'cust48', 'cust49', 'cust5', 'cust50', 'cust51', 'cust52', 'cust53', 'cust54', 'cust55', 'cust56', 'cust57',
        'cust58', 'cust59', 'cust6', 'cust60', 'cust61', 'cust62', 'cust63', 'cust64', 'cust65', 'cust66', 'cust67', 'cust68', 'cust69',
        'cust7', 'cust70', 'cust71', 'cust72', 'cust73', 'cust74', 'cust75', 'cust76', 'cust77', 'cust78', 'cust79', 'cust8', 'cust80',
        'cust81', 'cust82', 'cust83', 'cust84', 'cust85', 'cust86', 'cust87', 'cust88', 'cust89', 'cust9', 'cust90', 'cust91', 'cust92',
        'cust93', 'cust94', 'cust95', 'cust96', 'cust97', 'cust98', 'cust99', 'customer', 'customers', 'cv', 'cvs', 'cx', 'cy', 'cz',
        'd', 'dallas', 'data', 'database', 'database01', 'database02', 'database1', 'database2', 'databases', 'datastore', 'datos',
        'david', 'db', 'db0', 'db01', 'db02', 'db1', 'db2', 'dc', 'de', 'dealers', 'dec', 'def', 'default', 'defiant', 'delaware',
        'dell', 'delta', 'delta1', 'demo', 'demonstration', 'demos', 'denver', 'depot', 'des', 'desarrollo', 'descargas', 'design',
        'designer', 'detroit', 'dev', 'dev0', 'dev01', 'dev1', 'devel', 'develop', 'developer', 'developers', 'development', 'device','devserver',
        'devsql', 'dhcp', 'dial', 'dialup', 'digital', 'dilbert', 'dir', 'direct', 'directory', 'disc', 'discovery', 'discuss','discussion',
        'discussions', 'disk', 'disney', 'distributer', 'distributers', 'dj', 'dk', 'dm', 'dmail', 'dmz', 'dnews', 'dns', 'dns-2', 'dns0',
        'dns1', 'dns2', 'dns3', 'do', 'docs', 'documentacion', 'documentos', 'domain', 'domains', 'dominio', 'domino', 'dominoweb','doom',
        'download', 'downloads', 'downtown', 'dragon', 'drupal', 'dsl', 'dyn', 'dynamic', 'dynip', 'dz', 'e', 'e-com', 'e-commerce', 'e0',
        'eagle', 'earth', 'east', 'ec', 'echo', 'ecom', 'ecommerce', 'edi', 'edu', 'education', 'edward', 'ee', 'eg', 'eh', 'ejemplo','elpaso',
        'email', 'employees', 'empresa', 'empresas', 'en', 'enable', 'eng', 'eng01', 'eng1', 'engine', 'engineer', 'engineering',
        'enterprise', 'epsilon', 'er', 'erp', 'es', 'esd', 'esm', 'espanol', 'estadisticas', 'esx', 'et', 'eta', 'europe', 'events',
        'domain', 'exchange', 'exec', 'extern', 'external', 'extranet', 'f', 'f5', 'falcon', 'farm', 'faststats', 'fax', 'feedback',
        'feeds', 'fi', 'field', 'file', 'files', 'fileserv', 'fileserver', 'filestore', 'filter', 'find', 'finger', 'firewall', 'fix',
        'fixes', 'fj', 'fk', 'fl', 'flash', 'florida', 'flow', 'fm', 'fo', 'foobar', 'formacion', 'foro', 'foros', 'fortworth', 'forum',
        'forums', 'foto', 'fotos', 'foundry', 'fox', 'foxtrot', 'fr', 'france', 'frank', 'fred', 'freebsd', 'freebsd0', 'freebsd01',
        'freebsd02', 'freebsd1', 'freebsd2', 'freeware', 'fresno', 'front', 'frontdesk', 'fs', 'fsp', 'ftp', 'ftp-', 'ftp0', 'ftp2',
        'ftp_', 'ftpserver', 'fw', 'fw-1', 'fw1', 'fwsm', 'fwsm0', 'fwsm01', 'fwsm1', 'g', 'ga', 'galeria', 'galerias', 'galleries',
        'gallery', 'games', 'gamma', 'gandalf', 'gate', 'gatekeeper', 'gateway', 'gauss', 'gd', 'ge', 'gemini', 'general', 'george', 'georgia', 'germany', 'gf', 'gg', 'gh', 'gi', 'gl', 'glendale', 'gm', 'gmail', 'gn', 'go', 'gold', 'goldmine', 'golf',
        'gopher', 'gp', 'gq', 'gr', 'green', 'group', 'groups', 'groupwise', 'gs', 'gsx', 'gt', 'gu', 'guest', 'gw', 'gw1', 'gy', 'h',
        'hal', 'halflife', 'hawaii', 'hello', 'help', 'helpdesk', 'helponline', 'henry', 'hermes', 'hi', 'hidden', 'hk', 'hm', 'hn',
        'hobbes', 'hollywood', 'home', 'homebase', 'homer', 'honeypot', 'honolulu', 'host', 'host1', 'host3', 'host4', 'host5',
        'hotel', 'hotjobs', 'houstin', 'houston', 'howto', 'hp', 'hpov', 'hr', 'ht', 'http', 'https', 'hu', 'hub', 'humanresources', 'i',
        'ia', 'ias', 'ibm', 'ibmdb', 'id', 'ida', 'idaho', 'ids', 'ie', 'iis', 'il', 'illinois', 'im', 'image', 'images', 'imail', 'imap',
        'imap4', 'img', 'img0', 'img01', 'img02', 'in', 'inbound', 'inc', 'include', 'incoming', 'india', 'indiana', 'indianapolis',
        'info', 'informix', 'inside', 'install', 'int', 'intern', 'internal', 'international', 'internet', 'intl', 'intranet', 'invalid',
        'investor', 'investors', 'invia', 'invio', 'io', 'iota', 'iowa', 'iplanet', 'ipmonitor', 'ipsec', 'ipsec-gw', 'iq', 'ir', 'irc',
        'ircd', 'ircserver', 'ireland', 'iris', 'irvine', 'irving', 'is', 'isa', 'isaserv', 'isaserver', 'ism', 'israel', 'isync', 'it',
        'italy', 'ix', 'j', 'japan', 'java', 'je', 'jedi', 'jenkins', 'jm', 'jo', 'jobs', 'john', 'jp', 'jrun', 'juegos', 'juliet',
        'juliette', 'juniper', 'k', 'kansas', 'kansascity', 'kappa', 'kb', 'ke', 'kentucky', 'kerberos', 'keynote', 'kg', 'kh', 'ki',
        'kilo', 'king', 'km', 'kn', 'knowledgebase', 'knoxville', 'koe', 'korea', 'kp', 'kr', 'ks', 'kw', 'ky', 'kz', 'l', 'la', 'lab',
        'laboratory', 'labs', 'lambda', 'lan', 'laptop', 'laserjet', 'lasvegas', 'launch', 'lb', 'lc', 'ldap', 'legal', 'leo', 'li',
        'lib', 'library', 'lima', 'lincoln', 'link', 'linux', 'linux0', 'linux01', 'linux02', 'linux1', 'linux2', 'lista', 'lists',
        'listserv', 'listserver', 'live', 'lk', 'load', 'loadbalancer', 'local', 'localhost', 'log', 'log0', 'log01', 'log02', 'log1',
        'log2', 'logfile', 'logfiles', 'logger', 'logging', 'loghost', 'login', 'logs', 'london', 'longbeach', 'losangeles', 'lotus',
        'louisiana', 'lr', 'ls', 'lt', 'lu', 'luke', 'lv', 'ly', 'lyris', 'm', 'ma', 'mac', 'mac1', 'mac10', 'mac11', 'mac2', 'mac3',
        'mac4', 'mac5', 'mach', 'macintosh', 'madrid', 'mail', 'mail2', 'mailer', 'mailgate', 'mailhost', 'mailing', 'maillist',
        'maillists', 'mailroom', 'mailserv', 'mailsite', 'mailsrv', 'main', 'maine', 'maint', 'mall', 'manage', 'management', 'manager',
        'manufacturing', 'map', 'mapas', 'maps', 'marketing', 'marketplace', 'mars', 'marvin', 'mary', 'maryland', 'massachusetts',
        'master', 'max', 'mc', 'mci', 'md', 'mdaemon', 'me', 'media', 'member', 'members', 'memphis', 'mercury', 'merlin', 'messages',
        'messenger', 'mg', 'mgmt', 'mh', 'mi', 'miami', 'michigan', 'mickey', 'midwest', 'mike', 'milwaukee', 'minneapolis', 'minnesota',
        'mirror', 'mis', 'mississippi', 'missouri', 'mk', 'ml', 'mm', 'mn', 'mngt', 'mo', 'mobile', 'mom', 'monitor', 'monitoring','montana',
        'moon', 'moscow', 'movies', 'mozart', 'mp', 'mp3', 'mpeg', 'mpg', 'mq', 'mr', 'mrtg', 'ms', 'ms-exchange', 'ms-sql', 'msexchange',
        'mssql', 'mssql0', 'mssql01', 'mssql1', 'mt', 'mta', 'mtu', 'mu', 'multimedia', 'music', 'mv', 'mw', 'mx', 'my', 'mysql',
        'mysql0', 'mysql01', 'mysql1', 'mz', 'n', 'na', 'name', 'names', 'nameserv', 'nameserver', 'nas', 'nashville', 'nat', 'nc', 'nd',
        'nds', 'ne', 'nebraska', 'neptune', 'net', 'netapp', 'netdata', 'netgear', 'netmeeting', 'netscaler', 'netscreen', 'netstats',
        'network', 'nevada', 'new', 'newhampshire', 'newjersey', 'newmexico', 'neworleans', 'news', 'newsfeed', 'newsfeeds', 'newsgroups',
        'newton', 'newyork', 'newzealand', 'nf', 'ng', 'nh', 'ni', 'nigeria', 'nj', 'nl', 'nm', 'nms', 'nntp', 'no', 'node', 'nokia',
        'nombres', 'nora', 'north', 'northcarolina', 'northdakota', 'northeast', 'northwest', 'noticias', 'novell', 'november', 'np',
        'nr', 'ns', 'ns-', 'ns0', 'ns01', 'ns02', 'ns1', 'ns2', 'ns3', 'ns4', 'ns5', 'ns_', 'nt', 'nt4', 'nt40', 'ntmail', 'ntp',
        'ntserver', 'nu', 'null', 'nv', 'ny', 'nz', 'o', 'oakland', 'ocean', 'odin', 'office', 'offices', 'oh', 'ohio', 'ok', 'oklahoma',
        'oklahomacity', 'old', 'om', 'omaha', 'omega', 'omicron', 'online', 'ontario', 'open', 'openbsd', 'openview', 'operations', 'ops',
        'ops0', 'ops01', 'ops02', 'ops1', 'ops2', 'opsware', 'or', 'oracle', 'orange', 'order', 'orders', 'oregon', 'orion', 'orlando',
        'oscar', 'out', 'outbound', 'outgoing', 'outlook', 'outside', 'ov', 'owa', 'owa01', 'owa02', 'owa1', 'owa2', 'ows', 'oxnard', 'p',
        'pa', 'page', 'pager', 'pages', 'paginas', 'papa', 'paris', 'parners', 'partner', 'partners', 'patch', 'patches', 'paul',
        'payroll', 'pbx', 'pc', 'pc01', 'pc1', 'pc10', 'pc101', 'pc11', 'pc12', 'pc13', 'pc14', 'pc15', 'pc16', 'pc17', 'pc18', 'pc19',
        'pc2', 'pc20', 'pc21', 'pc22', 'pc23', 'pc24', 'pc25', 'pc26', 'pc27', 'pc28', 'pc29', 'pc3', 'pc30', 'pc31', 'pc32', 'pc33',
        'pc34', 'pc35', 'pc36', 'pc37', 'pc38', 'pc39', 'pc4', 'pc40', 'pc41', 'pc42', 'pc43', 'pc44', 'pc45', 'pc46', 'pc47', 'pc48',
        'pc49', 'pc5', 'pc50', 'pc51', 'pc52', 'pc53', 'pc54', 'pc55', 'pc56', 'pc57', 'pc58', 'pc59', 'pc6', 'pc60', 'pc7', 'pc8', 'pc9',
        'pcmail', 'pda', 'pdc', 'pe', 'pegasus', 'pennsylvania', 'peoplesoft', 'personal', 'pf', 'pg', 'pgp', 'ph', 'phi', 'philadelphia',
        'phoenix', 'phoeniz', 'phone', 'phones', 'photos', 'pi', 'pics', 'picture', 'pictures', 'pink', 'pipex-gw', 'pittsburgh', 'pix',
        'pk', 'pki', 'pl', 'plano', 'platinum', 'pluto', 'pm', 'pm1', 'pn', 'po', 'policy', 'polls', 'pop', 'pop3', 'portal', 'portals',
        'portfolio', 'portland', 'post', 'posta', 'posta01', 'posta02', 'posta03', 'postales', 'postoffice', 'ppp1', 'ppp10', 'ppp11',
        'ppp12', 'ppp13', 'ppp14', 'ppp15', 'ppp16', 'ppp17', 'ppp18', 'ppp19', 'ppp2', 'ppp20', 'ppp21', 'ppp3', 'ppp4', 'ppp5', 'ppp6',
        'ppp7', 'ppp8', 'ppp9', 'pptp', 'pr', 'prensa', 'press', 'priv', 'privacy', 'private', 'problemtracker', 'products', 'profiles',
        'project', 'projects', 'promo', 'proxy', 'prueba', 'pruebas', 'ps', 'psi', 'pss', 'pt', 'pub', 'public', 'pubs', 'purple', 'pw',
        'py', 'q', 'qa', 'qmail', 'qotd', 'quake', 'quebec', 'queen', 'quotes', 'r', 'r01', 'r02', 'r1', 'r2', 'ra', 'radio', 'radius',
        'rapidsite', 'raptor', 'ras', 'rc', 'rcs', 'rd', 're', 'read', 'realserver', 'recruiting', 'red', 'redhat', 'ref', 'reference',
        'reg', 'register', 'registro', 'registry', 'regs', 'relay', 'rem', 'remote', 'remstats', 'reports', 'research', 'reseller',
        'reserved', 'resumenes', 'rho', 'rhodeisland', 'ri', 'ris', 'rmi', 'ro', 'robert', 'romeo', 'root', 'rose', 'route', 'router',
        'router1', 'rs', 'rss', 'rtelnet', 'rtr', 'rtr01', 'rtr1', 'ru', 'rune', 'rw', 'rwhois', 's', 's1', 's2', 'sa', 'sac',
        'sacramento', 'sadmin', 'safe', 'sales', 'saltlake', 'sam', 'san', 'sanantonio', 'sandiego', 'sanfrancisco', 'sanjose',
        'saskatchewan', 'saturn', 'sb', 'sbs', 'sc', 'scanner', 'schedules', 'scotland', 'scotty', 'sd', 'se', 'search', 'seattle', 'sec',
        'secret', 'secure', 'secured', 'securid', 'security', 'sendmail', 'seri', 'serv', 'serv2', 'server', 'server1', 'servers',
        'service', 'services', 'servicio', 'servidor', 'setup', 'sg', 'sh', 'shared', 'sharepoint', 'shareware', 'shipping', 'shop',
        'shoppers', 'shopping', 'si', 'siebel', 'sierra', 'sigma', 'signin', 'signup', 'silver', 'sim', 'sirius', 'site', 'sj', 'sk',
        'skywalker', 'sl', 'slackware', 'slmail', 'sm', 'smc', 'sms', 'smtp', 'smtphost', 'sn', 'sniffer', 'snmp', 'snmpd', 'snoopy',
        'snort', 'so', 'social', 'software', 'sol', 'solaris', 'solutions', 'soporte', 'source', 'sourcecode', 'sourcesafe', 'south',
        'southcarolina', 'southdakota', 'southeast', 'southwest', 'spain', 'spam', 'spider', 'spiderman', 'splunk', 'spock', 'spokane',
        'springfield', 'sqa', 'sql', 'sql0', 'sql01', 'sql1', 'sql7', 'sqlserver', 'squid', 'sr', 'ss', 'ssh', 'ssl', 'ssl0', 'ssl01',
        'ssl1', 'st', 'staff', 'stage', 'staging', 'start', 'stat', 'static', 'statistics', 'stats', 'stlouis', 'stock', 'storage',
        'store', 'storefront', 'streaming', 'stronghold', 'strongmail', 'studio', 'submit', 'subversion', 'sun', 'sun0', 'sun01', 'sun02',
        'sun1', 'sun2', 'superman', 'supplier', 'suppliers', 'support', 'sv', 'sw', 'sw0', 'sw01', 'sw1', 'sweden', 'switch',
        'switzerland', 'sy', 'sybase', 'sydney', 'sysadmin', 'sysback', 'syslog', 'syslogs', 'system', 'sz', 't', 'tacoma', 'taiwan',
        'talk', 'tampa', 'tango', 'tau', 'tc', 'tcl', 'td', 'team', 'tech', 'technology', 'techsupport', 'telephone', 'telephony',
        'telnet', 'temp', 'tennessee', 'terminal', 'terminalserver', 'termserv', 'test', 'test2k', 'testbed', 'testing', 'testlab',
        'testlinux', 'testo', 'testserver', 'testsite', 'testsql', 'testxp', 'texas', 'tf', 'tftp', 'tg', 'th', 'thailand', 'theta',
        'thor', 'tienda', 'tiger', 'time', 'titan', 'tivoli', 'tj', 'tk', 'tm', 'tn', 'to', 'tokyo', 'toledo', 'tom', 'tool', 'tools',
        'toplayer', 'toronto', 'tour', 'tp', 'tr', 'tracker', 'train', 'training', 'transfers', 'trinidad', 'trinity', 'ts', 'ts1', 'tt',
        'tucson', 'tulsa', 'tumb', 'tumblr', 'tunnel', 'tv', 'tw', 'tx', 'tz', 'u', 'ua', 'uddi', 'ug', 'uk', 'um', 'uniform', 'union',
        'unitedkingdom', 'unitedstates', 'unix', 'unixware', 'update', 'updates', 'upload', 'ups', 'upsilon', 'uranus', 'urchin', 'us', 'usa', 'usenet', 'user', 'users', 'ut', 'utah', 'utilities', 'uy', 'uz', 'v', 'va', 'vader', 'vantive', 'vault', 'vc', 've',
        'vega', 'vegas', 'vend', 'vendors', 'venus', 'vermont', 'vg', 'vi', 'victor', 'video', 'videos', 'viking', 'violet', 'vip',
        'virginia', 'vista', 'vm', 'vmserver', 'vmware', 'vn', 'vnc', 'voice', 'voicemail', 'voip', 'voyager', 'vpn', 'vpn0', 'vpn01',
        'vpn02', 'vpn1', 'vpn2', 'vt', 'vu', 'w', 'w1', 'w2', 'w3', 'wa', 'wais', 'wallet', 'wam', 'wan', 'wap', 'warehouse', 'washington',
        'wc3', 'web', 'webaccess', 'webadmin', 'webalizer', 'webboard', 'webcache', 'webcam', 'webcast', 'webdev', 'webdocs', 'webfarm',
        'webhelp', 'weblib', 'weblogic', 'webmail', 'webmaster', 'webproxy', 'webring', 'webs', 'webserv', 'webserver', 'webservices',
        'website', 'websites', 'websphere', 'websrv', 'websrvr', 'webstats', 'webstore', 'websvr', 'webtrends', 'welcome', 'west',
        'westvirginia', 'wf', 'whiskey', 'white', 'whois', 'wi', 'wichita', 'wiki', 'wililiam', 'win', 'win01', 'win02', 'win1', 'win2',
        'win2000', 'win2003', 'win2k', 'win2k3', 'windows', 'windows01', 'windows02', 'windows1', 'windows2', 'windows2000', 'windows2003','windowsxp',
        'wingate', 'winnt', 'winproxy', 'wins', 'winserve', 'winxp', 'wire', 'wireless', 'wisconsin', 'wlan', 'wordpress', 'work', 'world',
        'write', 'ws', 'ws1', 'ws10', 'ws11', 'ws12', 'ws13', 'ws2', 'ws3', 'ws4', 'ws5', 'ws6', 'ws7', 'ws8', 'ws9', 'wusage', 'wv', 'ww','www', 'www-',
        'www-01', 'www-02', 'www-1', 'www-2', 'www-int', 'www0', 'www01', 'www02', 'www1', 'www2', 'www3', 'www_', 'wwwchat', 'wwwdev',
        'wwwmail', 'wy', 'wyoming', 'x', 'x-ray', 'xi', 'xlogan', 'xmail', 'xml', 'xp', 'y', 'yankee', 'ye', 'yellow', 'young', 'yt', 'yu',
        'z', 'z-log', 'za', 'zebra', 'zera', 'zeus', 'zlog', 'zm', 'zulu', 'zw', 'aaa', 'aarp', 'abb', 'abbott', 'abbvie', 'able', 'abogado',
        'abudhabi', 'ac', 'academy', 'accenture', 'accountant', 'accountants', 'aco', 'active', 'actor', 'ad', 'adac', 'ads', 'adult', 'ae',
        'aeg', 'aero', 'aetna', 'af', 'afl', 'ag', 'agakhan', 'agency', 'ai', 'aig', 'airbus', 'airforce', 'airtel', 'akdn', 'al', 'alibaba',
        'alipay','allfinanz', 'allstate', 'ally', 'alsace', 'alstom', 'am', 'amica', 'amsterdam', 'analytics', 'android', 'anquan', 'anz',
        'ao', 'apartments', 'app', 'apple', 'aq', 'aquarelle', 'ar', 'aramco', 'archi', 'army', 'arpa', 'art', 'arte', 'as', 'asia', 'associates', 'at', 'attorney', 'au', 'auction', 'audi', 'audible', 'audio', 'author', 'auto', 'autos', 'avianca', 'aw', 'aws',
        'ax', 'axa', 'az', 'azure', 'ba', 'baby', 'baidu', 'band', 'bank', 'bar', 'barcelona', 'barclaycard', 'barclays', 'barefoot',
        'bargains', 'bauhaus', 'bayern', 'bb', 'bbc', 'bbt', 'bbva', 'bcg', 'bcn', 'bd', 'be', 'beats', 'beauty', 'beer', 'bentley',
        'berlin', 'best', 'bestbuy', 'bet', 'bf', 'bg', 'bh', 'bharti', 'bi', 'bible', 'bid', 'bike', 'bing', 'bingo', 'bio', 'biz',
        'bj', 'black', 'blackfriday', 'blanco', 'blog', 'bloomberg', 'blue', 'bm', 'bms', 'bmw', 'bn', 'bnl', 'bnpparibas', 'bo', 'boats',
        'boehringer', 'bom', 'bond', 'boo', 'book', 'boots', 'bosch', 'bostik', 'bot', 'boutique', 'br', 'bradesco', 'bridgestone',
        'broadway', 'broker', 'brother', 'brussels', 'bs', 'bt', 'budapest', 'bugatti', 'build', 'builders', 'business', 'buy', 'buzz','bv',
        'bw', 'by', 'bz', 'bzh', 'ca', 'cab', 'cafe', 'cal', 'call', 'cam', 'camera', 'camp', 'cancerresearch', 'canon', 'capetown',
        'capital', 'car', 'caravan', 'cards', 'care', 'career', 'careers', 'cars', 'cartier', 'casa', 'cash', 'casino', 'cat', 'catering',
        'cba', 'cbn', 'cbre', 'cc', 'cd', 'ceb', 'center', 'ceo', 'cern', 'cf', 'cfa', 'cfd', 'cg', 'ch', 'chanel', 'channel', 'chase',
        'chat', 'cheap', 'chintai', 'chloe', 'christmas', 'chrome', 'church', 'ci', 'cipriani', 'circle', 'cisco', 'citic', 'city',
        'cityeats', 'ck', 'cl', 'claims', 'cleaning', 'click', 'clinic', 'clinique', 'clothing', 'cloud', 'club', 'clubmed', 'cm','cn',
        'co', 'coach', 'codes', 'coffee', 'college', 'cologne', 'com', 'comcast', 'commbank', 'community', 'company', 'compare', 'computer',
        'comsec', 'condos', 'construction', 'consulting', 'contact', 'contractors', 'cooking', 'cookingchannel', 'cool', 'coop', 'corsica',
        'country', 'coupon', 'coupons', 'courses', 'cr', 'credit', 'creditcard', 'creditunion', 'cricket', 'crown', 'crs', 'cruises', 'csc',
        'cu', 'cuisinella', 'cv', 'cw', 'cx', 'cy', 'cymru', 'cyou', 'cz', 'dabur', 'dad', 'dance', 'date', 'dating', 'datsun', 'day',
        'dclk', 'dds', 'de', 'deal', 'dealer', 'deals', 'degree', 'delivery', 'dell', 'deloitte', 'delta', 'democrat', 'dental', 'dentist',
        'desi', 'design', 'dev', 'dhl', 'diamonds', 'diet', 'digital', 'direct', 'directory', 'discount', 'dj', 'dk', 'dm', 'dnp', 'do', 'docs',
        'dog', 'doha', 'domains', 'dot', 'download', 'drive', 'dtv', 'dubai', 'dunlop', 'dupont', 'durban', 'dvag', 'dz', 'earth', 'eat',
        'ec', 'edeka', 'edu', 'education', 'ee', 'eg', 'email', 'emerck', 'energy', 'engineer', 'engineering', 'enterprises', 'epost',
        'epson', 'equipment', 'er', 'ericsson', 'erni', 'es', 'esq', 'estate', 'et', 'eu', 'eurovision', 'eus', 'events', 'everbank',
        'exchange', 'expert', 'exposed', 'express', 'extraspace', 'fage', 'fail', 'fairwinds', 'faith', 'family', 'fan', 'fans', 'farm',
        'farmers', 'fashion', 'fast', 'fedex', 'feedback', 'ferrero', 'fi', 'film', 'final', 'finance', 'financial', 'fire', 'firestone',
        'firmdale', 'fish', 'fishing', 'fit', 'fitness', 'fj', 'fk', 'flickr', 'flights', 'flir', 'florist', 'flowers', 'flsmidth', 'fly',
        'fm', 'fo', 'foo', 'foodnetwork', 'football', 'ford', 'forex', 'forsale', 'forum', 'foundation', 'fox', 'fr', 'fresenius', 'frl',
        'frogans', 'frontdoor', 'frontier', 'ftr', 'fujitsu', 'fujixerox', 'fund', 'furniture', 'futbol', 'fyi', 'ga', 'gal', 'gallery', 'gallo', 'gallup', 'game', 'games', 'garden', 'gb', 'gbiz', 'gd', 'gdn', 'ge', 'gea', 'gent', 'genting', 'gf', 'gg', 'ggee',
        'gh', 'gi', 'gift', 'gifts', 'gives', 'giving', 'gl', 'glass', 'gle', 'global', 'globo', 'gm', 'gmail', 'gmbh', 'gmo', 'gmx', 'gn',
        'godaddy', 'gold', 'goldpoint', 'golf', 'goo', 'goodhands', 'goodyear', 'goog', 'google', 'gop', 'got', 'gov', 'gp', 'gq', 'gr',
        'grainger', 'graphics', 'gratis', 'green', 'gripe', 'group', 'gs', 'gt', 'gu', 'guardian', 'gucci', 'guge', 'guide', 'guitars',
        'guru', 'gw', 'gy', 'hamburg', 'hangout', 'haus', 'hdfcbank', 'health', 'healthcare', 'help', 'helsinki', 'here', 'hermes', 'hgtv',
        'hiphop', 'hisamitsu', 'hitachi', 'hiv', 'hk', 'hkt', 'hm', 'hn', 'hockey', 'holdings', 'holiday', 'homedepot', 'homegoods', 'homes',
        'homesense', 'honda', 'horse', 'host', 'hosting', 'hoteles', 'hotmail', 'house', 'how', 'hr', 'hsbc', 'ht', 'htc', 'hu', 'hyundai',
        'ibm', 'icbc', 'ice', 'icu', 'id', 'ie', 'ifm', 'iinet', 'ikano', 'il', 'im', 'imamat', 'imdb', 'immo', 'immobilien', 'in',
        'industries', 'infiniti', 'info', 'ing', 'ink', 'institute', 'insurance', 'insure', 'int', 'international', 'intuit', 'investments',
        'io', 'ipiranga', 'iq', 'ir', 'irish', 'is', 'iselect', 'ismaili', 'ist', 'istanbul', 'it', 'itau', 'itv', 'iwc', 'jaguar', 'java',
        'jcb', 'jcp', 'je', 'jetzt', 'jewelry', 'jlc', 'jll', 'jm', 'jmp', 'jnj', 'jo', 'jobs', 'joburg', 'jot', 'joy', 'jp', 'jpmorgan',
        'jprs', 'juegos', 'kaufen', 'kddi', 'ke', 'kerryhotels', 'kerrylogistics', 'kerryproperties', 'kfh', 'kg', 'kh', 'ki', 'kia',
        'kim', 'kinder', 'kindle', 'kitchen', 'kiwi', 'km', 'kn', 'koeln', 'komatsu', 'kosher', 'kp', 'kpmg', 'kpn', 'kr', 'krd', 'kred',
        'kuokgroup', 'kw', 'ky', 'kyoto', 'kz', 'la', 'lacaixa', 'lamborghini', 'lamer', 'lancaster', 'lancome', 'land', 'landrover',
        'lanxess', 'lasalle', 'lat', 'latrobe', 'law', 'lawyer', 'lb', 'lc', 'lds', 'lease', 'leclerc', 'lefrak', 'legal', 'lego', 'lexus',
        'lgbt', 'li', 'liaison', 'lidl', 'life', 'lifeinsurance', 'lifestyle', 'lighting', 'like', 'limited', 'limo', 'lincoln', 'linde',
        'link', 'lipsy', 'live', 'living', 'lixil', 'lk', 'loan', 'loans', 'locker', 'locus', 'lol', 'london', 'lotte', 'lotto', 'love',
        'lpl', 'lplfinancial', 'lr', 'ls', 'lt', 'ltd', 'ltda', 'lu', 'lundbeck', 'lupin', 'luxe', 'luxury', 'lv', 'ly', 'ma', 'macys',
        'madrid', 'maif', 'maison', 'makeup', 'man', 'management', 'mango', 'market', 'marketing', 'markets', 'marriott', 'marshalls',
        'mattel', 'mba', 'mc', 'md', 'me', 'med', 'media', 'meet', 'melbourne', 'meme', 'memorial', 'men', 'menu', 'meo', 'metlife', 'mg',
        'mh', 'miami', 'microsoft', 'mil', 'mini', 'mint', 'mit', 'mitsubishi', 'mk', 'ml', 'mlb', 'mls', 'mm', 'mma', 'mn', 'mo', 'mobi','mobily',
        'moda', 'moe', 'moi', 'mom', 'monash', 'money', 'montblanc', 'mormon', 'mortgage', 'moscow', 'motorcycles', 'mov', 'movie',
        'movistar', 'mp', 'mq', 'mr', 'ms', 'mt', 'mtn', 'mtpc', 'mtr', 'mu', 'museum', 'mutual', 'mutuelle', 'mv', 'mw', 'mx', 'my', 'mz'
        'na', 'nadex', 'nagoya', 'name', 'nationwide', 'natura', 'navy', 'nc', 'ne', 'nec', 'net', 'netbank', 'netflix', 'network',
        'neustar', 'new', 'news', 'next', 'nextdirect', 'nexus', 'nf', 'nfl', 'ng', 'ngo', 'nhk', 'ni', 'nico', 'nike', 'nikon', 'ninja',
        'nissan', 'nissay', 'nl', 'no', 'nokia', 'northwesternmutual', 'norton', 'now', 'nowruz', 'nowtv', 'np', 'nr', 'nra', 'nrw', 'ntt',
        'nu', 'nyc', 'nz', 'obi', 'office', 'okinawa', 'olayan', 'olayangroup', 'ollo', 'om', 'omega', 'one', 'ong', 'onl', 'online',
        'onyourside', 'ooo', 'oracle', 'orange', 'org', 'organic', 'orientexpress', 'origins', 'osaka', 'otsuka', 'ott', 'ovh', 'pa', 'page',
        'pamperedchef', 'panasonic', 'panerai', 'paris', 'pars', 'partners', 'parts', 'party', 'passagens', 'pccw', 'pe', 'pet', 'pf', 'pfizer',
        'pg','ph', 'pharmacy', 'philips', 'photo', 'photography', 'photos', 'physio', 'piaget', 'pics', 'pictet', 'pictures', 'pid', 'pin',
        'ping', 'pink', 'pioneer', 'pizza', 'pk', 'pl', 'place', 'play', 'playstation', 'plumbing', 'plus', 'pm', 'pn', 'pnc', 'pohl',
        'poker', 'politie', 'porn', 'post', 'pr', 'praxi', 'press', 'prime', 'pro', 'prod', 'productions', 'prof', 'progressive', 'promo',
        'properties', 'property', 'protection', 'ps', 'pt', 'pub', 'pw', 'pwc', 'py', 'qa', 'qpon','quebec', 'quest', 'racing', 're',
        'read', 'realestate', 'realtor', 'realty', 'recipes', 'red', 'redstone', 'redumbrella', 'rehab', 'reise', 'reisen', 'reit',
        'ren', 'rent', 'rentals', 'repair', 'report', 'republican', 'rest', 'restaurant', 'review', 'reviews', 'rexroth', 'rich',
        'richardli', 'ricoh', 'rio', 'rip', 'ro', 'rocher', 'rocks', 'rodeo', 'room', 'rs', 'rsvp', 'ru', 'ruhr', 'run', 'rw', 'rwe',
        'ryukyu', 'sa', 'saarland', 'safe', 'safety', 'sakura', 'sale', 'salon', 'samsung', 'sandvik', 'sandvikcoromant', 'sanofi', 'sap',
        'sapo', 'sarl', 'sas', 'save', 'saxo', 'sb', 'sbi', 'sbs', 'sc', 'sca', 'scb', 'schaeffler', 'schmidt', 'scholarships', 'school',
        'schule', 'schwarz', 'science', 'scor', 'scot', 'sd', 'se', 'seat', 'security', 'seek', 'select', 'sener', 'services', 'ses',
        'seven', 'sew', 'sex', 'sexy', 'sfr', 'sg', 'sh', 'shangrila', 'sharp', 'shaw', 'shell', 'shia', 'shiksha', 'shoes', 'shop',
        'shopping', 'shouji', 'show', 'shriram', 'si', 'silk', 'sina', 'singles', 'site', 'sj', 'sk', 'ski', 'skin', 'sky', 'skype', 'sl',
        'sm', 'smart', 'smile', 'sn', 'sncf', 'so', 'soccer', 'social', 'softbank', 'software', 'sohu', 'solar', 'solutions', 'song', 'sony', 'soy',
        'space', 'spiegel', 'spot', 'spreadbetting', 'sr', 'srl', 'st', 'stada', 'staples', 'star', 'starhub', 'statebank', 'statefarm',
        'statoil', 'stc', 'stcgroup', 'stockholm', 'storage', 'store', 'stream', 'studio', 'study', 'style', 'su', 'sucks', 'supplies',
        'supply', 'support', 'surf', 'surgery', 'suzuki', 'sv', 'swatch', 'swiss', 'sx', 'sy', 'sydney', 'symantec', 'systems', 'sz',
        'tab', 'taipei', 'talk', 'taobao', 'tatamotors', 'tatar', 'tattoo', 'tax', 'taxi', 'tc', 'tci', 'td', 'tdk', 'team', 'tech',
        'technology', 'tel', 'telecity', 'telefonica', 'temasek', 'tennis', 'teva', 'tf', 'tg', 'th', 'thd', 'theater', 'theatre', 'tiaa',
        'tickets', 'tienda', 'tiffany', 'tips', 'tires', 'tirol', 'tj', 'tjmaxx', 'tjx', 'tk', 'tkmaxx', 'tl', 'tm', 'tmall', 'tn', 'to',
        'today', 'tokyo', 'tools', 'top', 'toray', 'toshiba', 'total', 'tours', 'town', 'toyota', 'toys', 'tr', 'trade', 'trading',
        'training', 'travel', 'travelchannel', 'travelers', 'travelersinsurance', 'trust', 'trv', 'tt', 'tube', 'tui', 'tunes', 'tushu',
        'tv', 'tvs', 'tw', 'tz', 'ua', 'ubs', 'ug', 'uk', 'unicom', 'university', 'uno', 'uol', 'ups', 'us', 'uy', 'uz', 'va', 'vacations',
        'vana', 'vc', 've', 'vegas', 'ventures', 'verisign', 'versicherung', 'vet', 'vg', 'vi', 'viajes', 'video', 'vig', 'viking', 'villas',
        'vin', 'vip', 'virgin', 'vision', 'vista','vistaprint','viva','vivo','vlaanderen','vn','vodka','volkswagen','vote','voting',
        'voto', 'voyage', 'vu', 'vuelos', 'wales', 'walter', 'wang', 'wanggou', 'warman', 'watch', 'watches', 'weather', 'weatherchannel',
        'webcam', 'weber', 'website', 'wed', 'wedding', 'weibo', 'weir', 'wf', 'whoswho', 'wien', 'wiki', 'williamhill', 'win', 'windows',
        'wine', 'winners', 'wme', 'wolterskluwer', 'woodside', 'work', 'works', 'world', 'ws', 'wtc', 'wtf', 'xbox', 'xerox', 'xfinity',
        'xihuan', 'xin', 'xn--11b4c3d', 'xn--1ck2e1b', 'xn--1qqw23a', 'xn--30rr7y', 'xn--3bst00m', 'xn--3ds443g', 'xn--3e0b707e',
        'xn--3pxu8k', 'xn--42c2d9a', 'xn--45brj9c', 'xn--45q11c', 'xn--4gbrim', 'xn--55qw42g', 'xn--55qx5d', 'xn--5su34j936bgsg',
        'xn--5tzm5g', 'xn--6frz82g', 'xn--6qq986b3xl', 'xn--80adxhks', 'xn--80ao21a', 'xn--80asehdb', 'xn--80aswg', 'xn--8y0a063a'
        'xn--90a3ac', 'xn--90ae', 'xn--90ais', 'xn--9dbq2a', 'xn--9et52u', 'xn--9krt00a', 'xn--b4w605ferd', 'xn--bck1b9a5dre4c',
        'xn--c1avg', 'xn--c2br7g', 'xn--cck2b3b', 'xn--cg4bki', 'xn--clchc0ea0b2g2a9gcd', 'xn--czr694b', 'xn--czrs0t', 'xn--czru2d',
        'xn--d1acj3b', 'xn--d1alf', 'xn--e1a4c', 'xn--eckvdtc9d', 'xn--efvy88h', 'xn--estv75g', 'xn--fct429k', 'xn--fhbei',
        'xn--fiq228c5hs', 'xn--fiq64b', 'xn--fiqs8s', 'xn--fiqz9s', 'xn--fjq720a', 'xn--flw351e', 'xn--fpcrj9c3d', 'xn--fzc2c9e2c',
        'xn--fzys8d69uvgm', 'xn--g2xx48c', 'xn--gckr3f0f', 'xn--gecrj9c', 'xn--h2brj9c', 'xn--hxt814e', 'xn--i1b6b1a6a2e',
        'xn--imr513n', 'xn--io0a7i', 'xn--j1aef', 'xn--j1amh', 'xn--j6w193g', 'xn--jlq61u9w7b', 'xn--jvr189m', 'xn--kcrx77d1x4a', 'xn--kprw13d',
        'xn--kpry57d', 'xn--kpu716f', 'xn--kput3i', 'xn--l1acc', 'xn--lgbbat1ad8j', 'xn--mgb9awbf', 'xn--mgba3a3ejt',
        'xn--mgba3a4f16a', 'xn--mgba7c0bbn0a', 'xn--mgbaam7a8h', 'xn--mgbab2bd', 'xn--mgbayh7gpa', 'xn--mgbb9fbpob', 'xn--mgbbh1a71e',
        'xn--mgbc0a9azcg', 'xn--mgbca7dzdo', 'xn--mgberp4a5d4ar', 'xn--mgbpl2fh', 'xn--mgbt3dhd', 'xn--mgbtx2b', 'xn--mgbx4cd0ab',
        'xn--mix891f', 'xn--mk1bu44c', 'xn--mxtq1m', 'xn--ngbc5azd', 'xn--ngbe9e0a', 'xn--node', 'xn--nqv7f', 'xn--nqv7fs00ema',
        'xn--nyqy26a', 'xn--o3cw4h', 'xn--ogbpf8fl', 'xn--p1acf', 'xn--p1ai', 'xn--pbt977c', 'xn--pgbs0dh', 'xn--pssy2u', 'xn--q9jyb4c',
        'xn--qcka1pmc', 'xn--qxam', 'xn--rhqv96g', 'xn--rovu88b', 'xn--s9brj9c', 'xn--ses554g', 'xn--t60b56a', 'xn--tckwe', 'xn--unup4y',
        'xn--vermgensberater-ctb', 'xn--vermgensberatung-pwb', 'xn--vhquv', 'xn--vuq861b', 'xn--w4r85el8fhu5dnra', 'xn--w4rs40l',
        'xn--wgbh1c', 'xn--wgbl6a', 'xn--xhq521b', 'xn--xkc2al3hye2a', 'xn--xkc2dl3a5ee0h', 'xn--y9a3aq', 'xn--yfro4i67o', 'xn--ygbi2ammx',
        'xn--zfr164b', 'xperia', 'xxx', 'xyz', 'yachts', 'yahoo', 'yamaxun', 'yandex', 'ye', 'yodobashi', 'yoga', 'yokohama', 'you',
        'youtube', 'yt', 'yun', 'za', 'zappos', 'zara', 'zero', 'zip', 'zippo', 'zm', 'zone', 'zuerich', 'zw'
]
