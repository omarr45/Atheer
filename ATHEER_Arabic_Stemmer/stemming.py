from . import script
from .normalization import Arabic_normalization


class LightStemmer():
    light_prefixes = (u"بال", u"وال", u"كال", u"فال", u"لل", u"ال")
    light_suffixes = (u"ون", u"ين", u"وا", u"ات", u"ان", u"ها")

    proposed_prefixes = (u"بال", u"وال", u"كال", u"فال", u"لل",
                         u"ل", u"و", u"ال", u"ك", u"ب", u"ف", u"س",)

    proposed_suffixes = (u"ات", u"ون", u"هما", u"كما", u"ين", u"ان", u"وا",
                         u"ها", u"تا", u"تم", u"تن", u"كن", u"هن", u"ه", u"ي", u"ك", u"هم", u"ت", u"ا")

    # Tokens that are mis-stemmed by the algorithm
    saved_tokens = [u"كتاب",  u"كريه", u"حبة",
                    u"سكرتير", u"سكرتيرة", u"الى", u"معهم"]

    @staticmethod
    def get_stem(token, full=False):
        token = Arabic_normalization.normalize_token(token)

        if not script.is_arabic_word(token):
            return token

        if len(token) == 3:
            return token

        if len(token) > 3 and token[0] == script.WAW:
            token = token[1:]

        if token in LightStemmer.saved_tokens:
            return token

        wordlen = len(token)

        for pref in LightStemmer.proposed_prefixes:
            length = len(pref)
            if (wordlen > length + 1) and (token[:length] == pref):
                if(full):
                    token = token[:length] + '+' + token[length:]
                else:
                    token = token[length:]
                break

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

    @staticmethod
    def get_root(token):
        # Get all أإآ to be ا for easier implementation
        # Removes diacritics and punctuations
        token = Arabic_normalization.normalize_token(token)

        # remove light affixes:
        # a) prefixes
        for pref in LightStemmer.light_prefixes:
            length = len(pref)
            if (len(token) > length + 1) and (token[:length] == pref):
                token = token[length:]
                break

        # b) suffixes
        if len(token) > 3:
            wordlen = len(token)
            for suf in LightStemmer.light_suffixes:
                suflen = len(suf)
                if (wordlen > len(suf) + 1) and token.endswith(suf):
                    token = token[:wordlen - suflen]
                    wordlen = len(token)

        if token in LightStemmer.saved_tokens:
            return token

        newToken = LightStemmer.get_taf3eela(token)

        if len(token) > 3 and token.__eq__(newToken):
            newToken = LightStemmer.get_stem(token)
            newToken = LightStemmer.get_taf3eela(
                LightStemmer.get_stem(newToken))
        return newToken

    @staticmethod
    def get_taf3eela(token):

        if len(token) == 3:
            # صلة
            if token[2] == script.TEH_MARBUTA:
                return u"و" + token[0:2]
            return token

        elif len(token) == 4:
            # مفعل - افعل - يفعل - تفعل
            if token[0] == script.MEEM or token[0] == script.ALEF or token[0] == script.YEH or token[0] == script.TEH:
                return str(token[1]) + str(token[2]) + str(token[3])
            # فاعل
            elif token[1] == script.ALEF:
                return str(token[0]) + str(token[2]) + str(token[3])
            # فعال - فعول - فعيل
            elif token[2] == script.ALEF or token[2] == script.WAW or token[2] == script.YEH:
                return str(token[0]) + str(token[1]) + str(token[3])
            # فعلى - فعلي - فعلة
            elif token[3] == script.YEH or token[3] == script.ALEF_MAKSURA or token[3] == script.TEH_MARBUTA:
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
            # مفتعل
            if token[0] == script.MEEM and token[2] == script.TEH:
                return token[1] + token[3] + token[4]
            # فاعلة
            if token[1] == script.ALEF and token[4] == script.TEH_MARBUTA:
                return token[0] + token[2] + token[3]
            # افتعل
            if token[0] == script.ALEF and token[2] == script.TEH:
                return token[1] + token[3] + token[4]
            # يفتعل
            if token[0] == script.YEH and token[2] == script.TEH:
                return token[1] + token[3] + token[4]
            # يتفعل
            if token[0] == script.YEH and token[1] == script.TEH:
                return token[2] + token[3] + token[4]
            # افعال
            if token[0] == script.ALEF and token[3] == script.ALEF:
                return token[1] + token[2] + token[4]
            # انفعل
            if token[0] == script.ALEF and token[1] == script.NOON:
                return token[2] + token[3] + token[4]
            # تفاعل
            if token[0] == script.TEH and token[2] == script.ALEF:
                return token[1] + token[3] + token[4]
            # تفعلن
            if token[0] == script.TEH and token[4] == script.NOON:
                return token[1] + token[2] + token[3]
            # فعائل
            if token[2] == script.ALEF and token[3] == script.YEH_HAMZA:
                return token[0] + token[1] + token[4]
            # فعالة
            if token[2] == script.ALEF and token[4] == script.TEH_MARBUTA:
                return token[0] + token[1] + token[3]
            # فعيلة
            if token[2] == script.YEH and token[4] == script.TEH_MARBUTA:
                return token[0] + token[1] + token[3]
            # فعالى
            if token[2] == script.ALEF and token[4] == script.ALEF_MAKSURA:
                return token[0] + token[1] + token[3]
            # فعلان
            if token[3] == script.ALEF and token[4] == script.NOON:
                return token[0] + token[1] + token[2]
            # فعلاء
            if token[3] == script.ALEF and token[4] == script.HAMZA:
                return token[0] + token[1] + token[2]
            # فعلاء
            if token[2] == script.WAW and token[4] == script.TEH_MARBUTA:
                return token[0] + token[1] + token[3]
            # تفعيل
            if token[0] == script.TEH and token[3] == script.YEH:
                return token[1] + token[2] + token[4]

        elif len(token) == 6:
            # مفعلون
            if token[0] == script.MEEM and token[4] == script.WAW and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # مفعلين
            if token[0] == script.MEEM and token[4] == script.YEH and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # مفعلان
            if token[0] == script.MEEM and token[4] == script.ALEF and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # مستفعل
            if token[0] == script.MEEM and token[1] == script.SEEN and token[2] == script.TEH:
                return token[3] + token[4] + token[5]
            # استفعل
            if token[0] == script.ALEF and token[1] == script.SEEN and token[2] == script.TEH:
                return token[3] + token[4] + token[5]
            # متفاعل
            if token[0] == script.MEEM and token[1] == script.TEH and token[3] == script.ALEF:
                return token[2] + token[4] + token[5]
            # مفاعيل
            if token[0] == script.MEEM and token[2] == script.ALEF and token[4] == script.YEH:
                return token[1] + token[3] + token[5]
            # افتعال
            if token[0] == script.ALEF and token[2] == script.TEH and token[4] == script.ALEF:
                return token[1] + token[3] + token[5]
            # تفعلين
            if token[0] == script.TEH and token[4] == script.YEH and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # تفعلون
            if token[0] == script.TEH and token[4] == script.WAW and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # تفعلان
            if token[0] == script.TEH and token[4] == script.ALEF and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # يفعلان
            if token[0] == script.YEH and token[4] == script.ALEF and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # فاعلان
            if token[1] == script.ALEF and token[4] == script.ALEF and token[5] == script.NOON:
                return token[0] + token[2] + token[3]
            # يفعلون
            if token[0] == script.YEH and token[4] == script.WAW and token[5] == script.NOON:
                return token[1] + token[2] + token[3]
            # انفعلت
            if token[0] == script.ALEF and token[1] == script.NOON and token[5] == script.TEH:
                return token[2] + token[3] + token[4]

        elif len(token) == 7:
            # مفاعلون
            if token[0] == script.MEEM and token[2] == script.ALEF and token[5] == script.WAW and token[6] == script.NOON:
                return token[1] + token[3] + token[4]
            # مفاعلات
            if token[0] == script.MEEM and token[2] == script.ALEF and token[5] == script.ALEF and token[6] == script.TEH:
                return token[1] + token[3] + token[4]
            # تفاعلان
            if token[0] == script.TEH and token[2] == script.ALEF and token[5] == script.ALEF and token[6] == script.NOON:
                return token[1] + token[3] + token[4]
            # تفعيلات
            if token[0] == script.TEH and token[3] == script.YEH and token[5] == script.ALEF and token[6] == script.TEH:
                return token[1] + token[2] + token[4]
            # فعالتان
            if token[2] == script.ALEF and token[4] == script.TEH and token[5] == script.ALEF and token[6] == script.NOON:
                return token[0] + token[1] + token[3]
            # فعالتين
            if token[2] == script.ALEF and token[4] == script.TEH and token[5] == script.YEH and token[6] == script.NOON:
                return token[0] + token[1] + token[3]

        elif len(token) == 8:
            # مستفعلات
            if token[0] == script.MEEM and token[1] == script.SEEN and token[2] == script.TEH and token[6] == script.ALEF and token[7] == script.TEH:
                return token[3] + token[4] + token[5]
            # مستفعلون
            if token[0] == script.MEEM and token[1] == script.SEEN and token[2] == script.TEH and token[6] == script.WAW and token[7] == script.NOON:
                return token[3] + token[4] + token[5]
            # مستفعلين
            if token[0] == script.MEEM and token[1] == script.SEEN and token[2] == script.TEH and token[6] == script.YEH and token[7] == script.NOON:
                return token[3] + token[4] + token[5]
            # متفاعلات
            if token[0] == script.MEEM and token[1] == script.TEH and token[3] == script.ALEF and token[6] == script.ALEF and token[7] == script.TEH:
                return token[2] + token[4] + token[5]

        return token


if __name__ == '__main__':
    pass
