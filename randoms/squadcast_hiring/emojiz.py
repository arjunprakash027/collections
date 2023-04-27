import urllib.parse
import emoji
import re
from cryptography.fernet import Fernet

key = b'dg0fOLKdmYTh2J1pNEDzniS530VuG8eaVcZ_4fTpuTc='
cipher = Fernet(key)
text = b'gAAAAABkSfoljg3fbadwEZxz1QGXBaqams9RgRyBTnzUpmDYKcDnyBCQh4iAw2VqhPEqT_jfVf0ujNb42q6X91dgGWqBSnWGk92IIMgEJYRNr93KOFs2u2QVz0t2J3PJI5aqEfElHEqOhgOzKnO_XbxdjbjLxIMpN2ZJVBQyS9Eq8MWcc2s9aK1wHP0rB1wvtLv3GGtiUYu0itXORVIEoYpVcnbfpfAIgI2nd_jLT-XdgsB3_9OEX05rGKebIF6PE9Kovsl_OLHcH04o-G1dtvJCHNibxlYXLCSS7AsjuMgYl3vKqMoypw632KqlWcN-zzg6enzhItyBSTmT20s095HEhGvRoSklfr_mfNl7v8Fvh48Hl_nNM4rezCqRa83JrQGo1CdpfBI1X6BnG-a___IDVKtBz9_UBEY8oe-dcX1w-jNl5LL9xnE1UjmaGem2ddAAwndSpV4-a2SD9GAiGBNvWb_sqbFTtcCaAEBwCk7xtWY90oYR5tGnz4ELQdVQhB3ZGHGWQQs6MnTG_3JZ4t55l9FhKdip12-UQvMddneowJOpxsaVyf44mhLYNpjleWkzVHSOp9M1pGsqBWJvuzoBs_FMLbmomOmp47GmRgr3qk8TQymH4k5sGWrdxsiRAJFDnw8f5JgXn-A-mNO7wjT3wzKpwg4xjtCpFWneBKA39HKGsAt03uDM_yIbcwKk5JRqC_aZg8RLcgu1C-Q1MRpnyQinngzDwB2jPTdi6ukSeVAPRFlZwTeHLXaUo0GfSA0jrcmJOqQ8fe8CQvBuMDgvPGD5qSgV26KZqZM3Z2-gCgIPyFSVQa62IyIcLRqnJuEJ_hm5V70IIJ_HG81wYllFT4Dwab0vtVwzZPS_JS_P1R7xdc2Bh8FvUOINL73F-a7eZ28uYG6KBmpI2bbktksVwq0ydk4Dcvs57ilWtEab_IEVlJ1R-qrlZvYaD6ciJEjkqFKewj4-WoeGXxCJfF3o1L1ajU_6Bg=='
decrypted_str = cipher.decrypt(text)
decrypted_str = decrypted_str.decode('utf-8')

def convert_to_emoji(unicode_str):

    word_lis = [x for x in unicode_str.split()]
    final_str = ''

    for x in word_lis:
        if x.startswith('U+'):
            final_str += chr(int(x[2:],16)) + ' '
        else:
            final_str += x + ' '
    print(final_str)

    url_encoded_str = urllib.parse.quote(unicode_str)
    
    return url_encoded_str

print(convert_to_emoji(decrypted_str))

