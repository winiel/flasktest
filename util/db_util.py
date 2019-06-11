import pymysql as pymysql


class DbUtil(object) :

    connection = None;
    cursor = None;

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'product',  # DB명
            'USER': 'abitree',  # 데이터베이스 계정
            'PASSWORD': 'abitree123',  # 계정 비밀번호
            'HOST': 'abitree.ccaniqrc8qkw.ap-northeast-2.rds.amazonaws.com',  # 데이테베이스 주소(IP)
            'PORT': 3306,  # 데이터베이스 포트(보통은 3306)
        },
        'slave': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'product',  # DB명
            'USER': 'abitree',  # 데이터베이스 계정
            'PASSWORD': 'abitree123',  # 계정 비밀번호
            # 'HOST': 'abitree-read.ccaniqrc8qkw.ap-northeast-2.rds.amazonaws.com',  # 데이테베이스 주소(IP)
            'HOST': 'abitree.ccaniqrc8qkw.ap-northeast-2.rds.amazonaws.com',  # 데이테베이스 주소(IP)
            'PORT': 3306,  # 데이터베이스 포트(보통은 3306)
        },
        'dev': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'product',  # DB명
            'USER': 'abitree',  # 데이터베이스 계정
            'PASSWORD': 'abitree123',  # 계정 비밀번호
            'HOST': '220.75.248.184',  # 데이테베이스 주소(IP)
            'PORT': 13306,  # 데이터베이스 포트(보통은 3306)
        }
    }


    def exeQuery(self, query, data=None):


        query = str(query).strip();
        queryTypePoint = query.find(" ");
        queryType = query[0:queryTypePoint];

        reVal = None;

        if queryType.lower() == "select" :
            reVal = self.exeGet(query, data);
            pass;
        elif queryType.lower() == "insert" :
            self.exeSet(query, data);
            pass;
        elif queryType.lower() == "update" :
            self.exeSet(query, data);
            pass;
        elif queryType.lower() == "delete" :
            self.exeSet(query, data);
            pass;

        else :
            pass;



        return reVal;



    def exeGet(self, query, data):
        dbSelector = "dev";
        # dbSelector = "slave";
        self.connection = pymysql.connect(host=self.DATABASES[dbSelector]["HOST"], port=self.DATABASES[dbSelector]["PORT"], user=self.DATABASES[dbSelector]["USER"], password=self.DATABASES[dbSelector]["PASSWORD"], db=self.DATABASES[dbSelector]["NAME"], charset='utf8')
        self.cursor = self.connection.cursor();

        c = self.cursor;
        c.execute(query, data);

        fieldnames = [name[0] for name in c.description];

        data = c.fetchall();

        reVal = [];

        if len(data) > 0:
            for row in data :
                reValColume = {};
                cntColume = 0;
                for rowColume in row:
                    reValColume[fieldnames[cntColume]] = rowColume;
                    cntColume+=1;

                    pass;
                pass;

                reVal.append(reValColume);
            pass;


        self.connection.close();
        return reVal;

    def exeSet(self, query, data):
        dbSelector = "dev";
        # dbSelector = "default";
        self.connection = pymysql.connect(host=self.DATABASES[dbSelector]["HOST"], port=self.DATABASES[dbSelector]["PORT"], user=self.DATABASES[dbSelector]["USER"], password=self.DATABASES[dbSelector]["PASSWORD"], db=self.DATABASES[dbSelector]["NAME"], charset='utf8');
        self.cursor = self.connection.cursor();

        print('just executed:', (query, data))


        c = self.cursor;
        c.execute(query, data);
        self.connection.commit();

        self.connection.close();