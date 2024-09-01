class Secret:
    def __init__(sf, alfabet:str="") -> None:
        """
            Initialize the alphabet
        """
        if alfabet == "":
            sf.alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ 0123456789."

        else:
            sf.alf = alfabet
        sf.bit = sf.bit_length(len(sf.alf))

    def bit_length(sf, alfabet_len:int) -> int:
        """
            Returns the bit length of the binary representation of a character
        """
        bit_length = 0
        if (alfabet_len > 0) and (alfabet_len & (alfabet_len - 1)) == 0:

            while 2**bit_length != alfabet_len:
                bit_length += 1
        else:
            raise ValueError("The alphabet must contain a number of characters that is a power of two")
        return bit_length

    


test = Secret()
# len(test.alf) == 127
# test.bit == 7
