#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
created on 2014 Mar 28
by disooqi
'''
from . import script


class Stemmer:

    def __init__(self):
        pass


class LightStemmer(Stemmer):
    proposed_prefixes = (u"بال", u"وال", u"كال", u"فال", u"لل",
                         u"ل", u"و", u"ال", u"ك", u"ب", u"ف", u"س",)

    proposed_suffixes = (u"ات", u"ون", u"هما", u"كما", u"ين", u"ان", u"وا",
                         u"ها", u"تا", u"تم", u"تن", u"كن", u"هن", u"ه", u"ي", u"ك", u"هم", u"ت",)

    saved_tokens = [u"كتاب", u"وجه", u"كريه", u"سكرتير", u"سكرتيرة"]

    # larkey_defarticles = (u"ال", u"وال", u"بال", u"كال", u"فال", u"لل")

    # larkey_suffixes = (u"ها", u"ان", u"ات", u"ون", u"ين",
    #                    u"يه", u"ية", u"ه", u"ة", u"ي")

    def __init__(self):
        Stemmer.__init__(self)

    @staticmethod
    def get_root(token):
        if len(token) == 3:
            return token
        if len(token) == 4:
            # مفعل - افعل - يفعل
            if token[0] == script.MEEM or token[0] == script.ALEF or token[0] == script.YEH:
                return str(token[1]) + str(token[2]) + str(token[3])
            # فاعل
            elif token[1] == script.ALEF:
                return str(token[0]) + str(token[2]) + str(token[3])
            # فعال - فعول - فعيل
            elif token[2] == script.ALEF or token[2] == script.WAW or token[2] == script.YEH:
                return str(token[0]) + str(token[1]) + str(token[3])
            # فعلى - فعلي
            elif token[3] == script.YEH or token[3] == script.ALEF_MAKSURA:
                return str(token[0]) + str(token[1]) + str(token[2])
        elif len(token) == 5:
            # مفعول
            if token[0] == script.MEEM and token[3] == script.WAW:
                return token[1] + token[2] + token[4]
            # مفعال
            if token[0] == script.MEEM and token[3] == script.ALEF:
                return token[1] + token[2] + token[4]
            # مفعلة
            if token[0] == script.MEEM and token[4] == script.TEH_MARBUTA:
                return token[1] + token[2] + token[3]
            # مفاعل
            if token[0] == script.MEEM and token[2] == script.ALEF:
                return token[1] + token[3] + token[4]
            return token
        elif len(token) == 6:
            return token
        # token = LightStemmer.stem_token(token, full=False)
        return token

    @staticmethod
    def stem_token(token, full=False):
        ''' The method takes a valid Arabic word as a parameter and return a stemmed term '''
        if not script.isArabicword(token):
            return token

        if len(token) > 3 and token[:1] == script.WAW:
            token = token[1:]

        if token in LightStemmer.saved_tokens:
            return token

        length = 0
        wordlen = len(token)

        for pref in LightStemmer.proposed_prefixes:
            length = len(pref)
            if (wordlen > length + 1) and (token[:length] == pref):
                if(full):
                    token = token[:length] + '+' + token[length:]
                else:
                    token = token[length:]
                break

        # repeat 3 times on suffix (يكتبونها)
        # for _ in range(3):
        if len(token) > 3:
            wordlen = len(token)
            for suf in LightStemmer.proposed_suffixes:
                suflen = len(suf)
                if (wordlen > len(suf) + 1) and token.endswith(suf):
                    if (full):
                        token = token[:wordlen - suflen] + \
                            '+' + token[wordlen-suflen:]
                    else:
                        token = token[:wordlen - suflen]
                    wordlen = len(token)

        return token


if __name__ == '__main__':
    pass
