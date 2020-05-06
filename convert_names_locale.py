# %%
import json
import ast
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

# %%
fnames = open('./names_locale_iast.json', 'rt')
json_names = json.load(fnames)
out_names = dict()

# %%


def translate_indic_texts(data, fr, to):
    if isinstance(data, dict):
        d = dict()
        for k, v in data.items():
            if k == 'comments':
                d[k] = v
            else:
                d[k] = translate_indic_texts(v, fr, to)
        return d
    elif isinstance(data, list):
        d = []
        for v in data:
            d.append(translate_indic_texts(v, fr, to))
        return d
    else:
        try:
            return transliterate(data, fr, to)
        except:
            return data


# %%
out_names = translate_indic_texts(
    json_names, sanscript.IAST, sanscript.DEVANAGARI)
print(out_names)
# print(json.dumps(out_names))

# %%
fout = open('names_locale_sa.json', 'wt')
fout.write(json.dumps(obj=out_names, ensure_ascii=False))
fout.close()


# %%
# testing
test = dict(o='one', t='two')
print(test)

# %%
