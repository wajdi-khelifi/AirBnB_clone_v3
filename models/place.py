{"payload":{"allShortcutsEnabled":false,"fileTree":{"models":{"items":[{"name":"engine","path":"models/engine","contentType":"directory"},{"name":"__init__.py","path":"models/__init__.py","contentType":"file"},{"name":"amenity.py","path":"models/amenity.py","contentType":"file"},{"name":"base_model.py","path":"models/base_model.py","contentType":"file"},{"name":"city.py","path":"models/city.py","contentType":"file"},{"name":"place.py","path":"models/place.py","contentType":"file"},{"name":"review.py","path":"models/review.py","contentType":"file"},{"name":"state.py","path":"models/state.py","contentType":"file"},{"name":"user.py","path":"models/user.py","contentType":"file"}],"totalCount":9},"":{"items":[{"name":"api","path":"api","contentType":"directory"},{"name":"models","path":"models","contentType":"directory"},{"name":"tests","path":"tests","contentType":"directory"},{"name":"web_flask","path":"web_flask","contentType":"directory"},{"name":"web_static","path":"web_static","contentType":"directory"},{"name":"0-setup_web_static.sh","path":"0-setup_web_static.sh","contentType":"file"},{"name":"1-pack_web_static.py","path":"1-pack_web_static.py","contentType":"file"},{"name":"2-do_deploy_web_static.py","path":"2-do_deploy_web_static.py","contentType":"file"},{"name":"3-deploy_web_static.py","path":"3-deploy_web_static.py","contentType":"file"},{"name":"AUTHORS","path":"AUTHORS","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"console.py","path":"console.py","contentType":"file"},{"name":"setup_mysql_dev.sql","path":"setup_mysql_dev.sql","contentType":"file"},{"name":"setup_mysql_test.sql","path":"setup_mysql_test.sql","contentType":"file"}],"totalCount":14}},"fileTreeProcessingTime":5.146084,"foldersToFetch":[],"repo":{"id":538457494,"defaultBranch":"main","name":"holbertonschool-AirBnB_clone_v3","ownerLogin":"Karoline-S","currentUserCanPush":false,"isFork":true,"isEmpty":false,"createdAt":"2022-09-19T10:56:29.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/92977874?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1663924331.696432","canEdit":false,"refType":"branch","currentOid":"67108a2af89b7b6d39e48740ba57c9642995ec7c"},"path":"models/place.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python","\"\"\" holds class Place\"\"\"","import models","from models.base_model import BaseModel, Base","from os import getenv","import sqlalchemy","from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table","from sqlalchemy.orm import relationship","","if models.storage_t == 'db':","    place_amenity = Table('place_amenity', Base.metadata,","                          Column('place_id', String(60),","                                 ForeignKey('places.id', onupdate='CASCADE',","                                            ondelete='CASCADE'),","                                 primary_key=True),","                          Column('amenity_id', String(60),","                                 ForeignKey('amenities.id', onupdate='CASCADE',","                                            ondelete='CASCADE'),","                                 primary_key=True))","","","class Place(BaseModel, Base):","    \"\"\"Representation of Place \"\"\"","    if models.storage_t == 'db':","        __tablename__ = 'places'","        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)","        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)","        name = Column(String(128), nullable=False)","        description = Column(String(1024), nullable=True)","        number_rooms = Column(Integer, nullable=False, default=0)","        number_bathrooms = Column(Integer, nullable=False, default=0)","        max_guest = Column(Integer, nullable=False, default=0)","        price_by_night = Column(Integer, nullable=False, default=0)","        latitude = Column(Float, nullable=True)","        longitude = Column(Float, nullable=True)","        reviews = relationship(\"Review\", backref=\"place\")","        amenities = relationship(\"Amenity\", secondary=\"place_amenity\",","                                 backref=\"place_amenities\",","                                 viewonly=False)","    else:","        city_id = \"\"","        user_id = \"\"","        name = \"\"","        description = \"\"","        number_rooms = 0","        number_bathrooms = 0","        max_guest = 0","        price_by_night = 0","        latitude = 0.0","        longitude = 0.0","        amenity_ids = []","","    def __init__(self, *args, **kwargs):","        \"\"\"initializes Place\"\"\"","        super().__init__(*args, **kwargs)","","    if models.storage_t != 'db':","        @property","        def reviews(self):","            \"\"\"getter attribute returns the list of Review instances\"\"\"","            from models.review import Review","            review_list = []","            all_reviews = models.storage.all(Review)","            for review in all_reviews.values():","                if review.place_id == self.id:","                    review_list.append(review)","            return review_list","","        @property","        def amenities(self):","            \"\"\"getter attribute returns the list of Amenity instances\"\"\"","            from models.amenity import Amenity","            amenity_list = []","            all_amenities = models.storage.all(Amenity)","            for amenity in all_amenities.values():","                if amenity.place_id == self.id:","                    amenity_list.append(amenity)","            return amenity_list"],"stylingDirectives":[[{"start":0,"end":17,"cssClass":"pl-c"}],[{"start":0,"end":24,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":22,"cssClass":"pl-s1"},{"start":23,"end":29,"cssClass":"pl-k"},{"start":30,"end":39,"cssClass":"pl-v"},{"start":41,"end":45,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":21,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":17,"cssClass":"pl-s1"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":15,"cssClass":"pl-s1"},{"start":16,"end":22,"cssClass":"pl-k"},{"start":23,"end":29,"cssClass":"pl-v"},{"start":31,"end":37,"cssClass":"pl-v"},{"start":39,"end":46,"cssClass":"pl-v"},{"start":48,"end":53,"cssClass":"pl-v"},{"start":55,"end":65,"cssClass":"pl-v"},{"start":67,"end":72,"cssClass":"pl-v"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":15,"cssClass":"pl-s1"},{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":26,"cssClass":"pl-k"},{"start":27,"end":39,"cssClass":"pl-s1"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":9,"cssClass":"pl-s1"},{"start":10,"end":19,"cssClass":"pl-s1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-s"}],[{"start":4,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":25,"cssClass":"pl-v"},{"start":26,"end":41,"cssClass":"pl-s"},{"start":43,"end":47,"cssClass":"pl-v"},{"start":48,"end":56,"cssClass":"pl-s1"}],[{"start":26,"end":32,"cssClass":"pl-v"},{"start":33,"end":43,"cssClass":"pl-s"},{"start":45,"end":51,"cssClass":"pl-v"},{"start":52,"end":54,"cssClass":"pl-c1"}],[{"start":33,"end":43,"cssClass":"pl-v"},{"start":44,"end":55,"cssClass":"pl-s"},{"start":57,"end":65,"cssClass":"pl-s1"},{"start":65,"end":66,"cssClass":"pl-c1"},{"start":66,"end":75,"cssClass":"pl-s"}],[{"start":44,"end":52,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":53,"end":62,"cssClass":"pl-s"}],[{"start":33,"end":44,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":45,"end":49,"cssClass":"pl-c1"}],[{"start":26,"end":32,"cssClass":"pl-v"},{"start":33,"end":45,"cssClass":"pl-s"},{"start":47,"end":53,"cssClass":"pl-v"},{"start":54,"end":56,"cssClass":"pl-c1"}],[{"start":33,"end":43,"cssClass":"pl-v"},{"start":44,"end":58,"cssClass":"pl-s"},{"start":60,"end":68,"cssClass":"pl-s1"},{"start":68,"end":69,"cssClass":"pl-c1"},{"start":69,"end":78,"cssClass":"pl-s"}],[{"start":44,"end":52,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":53,"end":62,"cssClass":"pl-s"}],[{"start":33,"end":44,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":45,"end":49,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":11,"cssClass":"pl-v"},{"start":12,"end":21,"cssClass":"pl-v"},{"start":23,"end":27,"cssClass":"pl-v"}],[{"start":4,"end":34,"cssClass":"pl-s"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":26,"cssClass":"pl-c1"},{"start":27,"end":31,"cssClass":"pl-s"}],[{"start":8,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":32,"cssClass":"pl-s"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":24,"cssClass":"pl-v"},{"start":25,"end":31,"cssClass":"pl-v"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":37,"end":47,"cssClass":"pl-v"},{"start":48,"end":59,"cssClass":"pl-s"},{"start":62,"end":70,"cssClass":"pl-s1"},{"start":70,"end":71,"cssClass":"pl-c1"},{"start":71,"end":76,"cssClass":"pl-c1"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":24,"cssClass":"pl-v"},{"start":25,"end":31,"cssClass":"pl-v"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":37,"end":47,"cssClass":"pl-v"},{"start":48,"end":58,"cssClass":"pl-s"},{"start":61,"end":69,"cssClass":"pl-s1"},{"start":69,"end":70,"cssClass":"pl-c1"},{"start":70,"end":75,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":21,"cssClass":"pl-v"},{"start":22,"end":28,"cssClass":"pl-v"},{"start":29,"end":32,"cssClass":"pl-c1"},{"start":35,"end":43,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":44,"end":49,"cssClass":"pl-c1"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":28,"cssClass":"pl-v"},{"start":29,"end":35,"cssClass":"pl-v"},{"start":36,"end":40,"cssClass":"pl-c1"},{"start":43,"end":51,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-c1"},{"start":52,"end":56,"cssClass":"pl-c1"}],[{"start":8,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":29,"cssClass":"pl-v"},{"start":30,"end":37,"cssClass":"pl-v"},{"start":39,"end":47,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"},{"start":48,"end":53,"cssClass":"pl-c1"},{"start":55,"end":62,"cssClass":"pl-s1"},{"start":62,"end":63,"cssClass":"pl-c1"},{"start":63,"end":64,"cssClass":"pl-c1"}],[{"start":8,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":33,"cssClass":"pl-v"},{"start":34,"end":41,"cssClass":"pl-v"},{"start":43,"end":51,"cssClass":"pl-s1"},{"start":51,"end":52,"cssClass":"pl-c1"},{"start":52,"end":57,"cssClass":"pl-c1"},{"start":59,"end":66,"cssClass":"pl-s1"},{"start":66,"end":67,"cssClass":"pl-c1"},{"start":67,"end":68,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":26,"cssClass":"pl-v"},{"start":27,"end":34,"cssClass":"pl-v"},{"start":36,"end":44,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":45,"end":50,"cssClass":"pl-c1"},{"start":52,"end":59,"cssClass":"pl-s1"},{"start":59,"end":60,"cssClass":"pl-c1"},{"start":60,"end":61,"cssClass":"pl-c1"}],[{"start":8,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":31,"cssClass":"pl-v"},{"start":32,"end":39,"cssClass":"pl-v"},{"start":41,"end":49,"cssClass":"pl-s1"},{"start":49,"end":50,"cssClass":"pl-c1"},{"start":50,"end":55,"cssClass":"pl-c1"},{"start":57,"end":64,"cssClass":"pl-s1"},{"start":64,"end":65,"cssClass":"pl-c1"},{"start":65,"end":66,"cssClass":"pl-c1"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":25,"cssClass":"pl-v"},{"start":26,"end":31,"cssClass":"pl-v"},{"start":33,"end":41,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":42,"end":46,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":26,"cssClass":"pl-v"},{"start":27,"end":32,"cssClass":"pl-v"},{"start":34,"end":42,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":43,"end":47,"cssClass":"pl-c1"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":30,"cssClass":"pl-en"},{"start":31,"end":39,"cssClass":"pl-s"},{"start":41,"end":48,"cssClass":"pl-s1"},{"start":48,"end":49,"cssClass":"pl-c1"},{"start":49,"end":56,"cssClass":"pl-s"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":32,"cssClass":"pl-en"},{"start":33,"end":42,"cssClass":"pl-s"},{"start":44,"end":53,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":54,"end":69,"cssClass":"pl-s"}],[{"start":33,"end":40,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":41,"end":58,"cssClass":"pl-s"}],[{"start":33,"end":41,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":42,"end":47,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-s"}],[{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":20,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":15,"end":17,"cssClass":"pl-s"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":24,"cssClass":"pl-s"}],[{"start":8,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-c1"}],[{"start":8,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":28,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":8,"end":22,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-c1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":23,"cssClass":"pl-c1"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-s1"},{"start":30,"end":32,"cssClass":"pl-c1"},{"start":32,"end":38,"cssClass":"pl-s1"}],[{"start":8,"end":31,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":16,"end":24,"cssClass":"pl-en"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":26,"end":30,"cssClass":"pl-s1"},{"start":32,"end":34,"cssClass":"pl-c1"},{"start":34,"end":40,"cssClass":"pl-s1"}],[],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":23,"cssClass":"pl-s1"},{"start":24,"end":26,"cssClass":"pl-c1"},{"start":27,"end":31,"cssClass":"pl-s"}],[{"start":8,"end":17,"cssClass":"pl-en"},{"start":9,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":19,"cssClass":"pl-en"},{"start":20,"end":24,"cssClass":"pl-s1"}],[{"start":12,"end":71,"cssClass":"pl-s"}],[{"start":12,"end":16,"cssClass":"pl-k"},{"start":17,"end":23,"cssClass":"pl-s1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":31,"end":37,"cssClass":"pl-k"},{"start":38,"end":44,"cssClass":"pl-v"}],[{"start":12,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[{"start":12,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":33,"end":40,"cssClass":"pl-s1"},{"start":41,"end":44,"cssClass":"pl-en"},{"start":45,"end":51,"cssClass":"pl-v"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":37,"cssClass":"pl-s1"},{"start":38,"end":44,"cssClass":"pl-en"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":25,"cssClass":"pl-s1"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":35,"end":37,"cssClass":"pl-c1"},{"start":38,"end":42,"cssClass":"pl-s1"},{"start":43,"end":45,"cssClass":"pl-s1"}],[{"start":20,"end":31,"cssClass":"pl-s1"},{"start":32,"end":38,"cssClass":"pl-en"},{"start":39,"end":45,"cssClass":"pl-s1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":30,"cssClass":"pl-s1"}],[],[{"start":8,"end":17,"cssClass":"pl-en"},{"start":9,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":21,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-s1"}],[{"start":12,"end":72,"cssClass":"pl-s"}],[{"start":12,"end":16,"cssClass":"pl-k"},{"start":17,"end":23,"cssClass":"pl-s1"},{"start":24,"end":31,"cssClass":"pl-s1"},{"start":32,"end":38,"cssClass":"pl-k"},{"start":39,"end":46,"cssClass":"pl-v"}],[{"start":12,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"}],[{"start":12,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":34,"cssClass":"pl-s1"},{"start":35,"end":42,"cssClass":"pl-s1"},{"start":43,"end":46,"cssClass":"pl-en"},{"start":47,"end":54,"cssClass":"pl-v"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":23,"cssClass":"pl-s1"},{"start":24,"end":26,"cssClass":"pl-c1"},{"start":27,"end":40,"cssClass":"pl-s1"},{"start":41,"end":47,"cssClass":"pl-en"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":26,"cssClass":"pl-s1"},{"start":27,"end":35,"cssClass":"pl-s1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":43,"cssClass":"pl-s1"},{"start":44,"end":46,"cssClass":"pl-s1"}],[{"start":20,"end":32,"cssClass":"pl-s1"},{"start":33,"end":39,"cssClass":"pl-en"},{"start":40,"end":47,"cssClass":"pl-s1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":31,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Karoline-S/holbertonschool-AirBnB_clone_v3/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null},"displayName":"place.py","displayUrl":"https://github.com/Karoline-S/holbertonschool-AirBnB_clone_v3/blob/main/models/place.py?raw=true","headerInfo":{"blobSize":"3.05 KB","deleteTooltip":"You must be signed in to make or propose changes","editTooltip":"You must be signed in to make or propose changes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"gitLfsPath":null,"onBranch":true,"shortPath":"0aed5a7","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FKaroline-S%2Fholbertonschool-AirBnB_clone_v3%2Fblob%2Fmain%2Fmodels%2Fplace.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"78","truncatedSloc":"72"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Karoline-S/holbertonschool-AirBnB_clone_v3/blob/main/models/place.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Karoline-S/holbertonschool-AirBnB_clone_v3/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Karoline-S/holbertonschool-AirBnB_clone_v3/raw/main/models/place.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Karoline-S","repoName":"holbertonschool-AirBnB_clone_v3","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"Place","kind":"class","ident_start":859,"ident_end":864,"extent_start":853,"extent_end":3120,"fully_qualified_name":"Place","ident_utf16":{"start":{"line_number":21,"utf16_col":6},"end":{"line_number":21,"utf16_col":11}},"extent_utf16":{"start":{"line_number":21,"utf16_col":0},"end":{"line_number":77,"utf16_col":31}}},{"name":"__init__","kind":"function","ident_start":2129,"ident_end":2137,"extent_start":2125,"extent_end":2235,"fully_qualified_name":"Place.__init__","ident_utf16":{"start":{"line_number":52,"utf16_col":8},"end":{"line_number":52,"utf16_col":16}},"extent_utf16":{"start":{"line_number":52,"utf16_col":4},"end":{"line_number":54,"utf16_col":41}}},{"name":"reviews","kind":"function","ident_start":2300,"ident_end":2307,"extent_start":2296,"extent_end":2686,"fully_qualified_name":"Place.reviews","ident_utf16":{"start":{"line_number":58,"utf16_col":12},"end":{"line_number":58,"utf16_col":19}},"extent_utf16":{"start":{"line_number":58,"utf16_col":8},"end":{"line_number":66,"utf16_col":30}}},{"name":"amenities","kind":"function","ident_start":2718,"ident_end":2727,"extent_start":2714,"extent_end":3120,"fully_qualified_name":"Place.amenities","ident_utf16":{"start":{"line_number":69,"utf16_col":12},"end":{"line_number":69,"utf16_col":21}},"extent_utf16":{"start":{"line_number":69,"utf16_col":8},"end":{"line_number":77,"utf16_col":31}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Karoline-S/holbertonschool-AirBnB_clone_v3/branches":{"post":"afEnDJCpt5Qpd9bRloYW33epFUBQIW6KSXaPbiMWee_E4ZZhSUFd00BDi41tILz7TIBWIce2mM-ihwIRMW6Ydw"},"/repos/preferences":{"post":"g4S7DuMh9nOilJ1CgcSPPFA2W6ZESMw9kBWFFninlenYKXhs0XG9cj__LQ5BaR_EDzr-0zQ3PhzNG0yXehVFbg"}}},"title":"holbertonschool-AirBnB_clone_v3/models/place.py at main · Karoline-S/holbertonschool-AirBnB_clone_v3"}