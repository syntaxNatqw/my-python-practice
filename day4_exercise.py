words = ['Thirty', 'Days', 'Of', 'Python']
results = ' '.join(words)
print(results)

words = ['Coding', 'For', 'All']
results = ' '.join(words)
print(results)

company = "Coding For All"
print(company)
print(len(company))

print(company.upper()) # whoppsie i didnt know this
print(company.lower())

print('Coding For All'.capitalize())
print('Coding For All'.title())
print('Coding For All'.swapcase())

print(company[0:6])  # it should print 'coding' but idk how python work hahaha
print(company.find("Coding"))
print(company.replace('Coding','Sleeping'))

print('Python for Everyone'.replace('Everyone' , 'All'))

print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# uhh C?? wtf? or 6? 67?? (it was C you fucking dipshit)
print(company[0])
# dont have to ask me twice hahahaha
# fine im stupid i hate index and characters so much
print(company[13])
# A. if im wrong im gay
print(company[10])

# acronym là từ viết tắt omfg i hate english grgrgr im not coding this shit
print('PFE')
print('CFA')

print(company.index('C'))
print(company.index('F'))
# ui vãi cái này là nó bắt mình tìm từ phải sang trái, cái index là nó tìm từ trái sang phải
# td;dl thì yeahh muốn tìm chữ thì dùng rfind hoặc lfind
print('Coding For All People'.rfind('l')) 
print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

# miss gemini helped me this hah

sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = 'because because because'

# hãy để python tìm xem cụm từ bắt đầu từ đâu.
start = sentence.find(phrase)
# cộng độ dài của cụm từ để tìm ra điểm kết thúc của nó. (what??)
end = start + len(phrase)
# SLICE KO DÙNG NGOẶC TRÒN
# SLICE KO DÙNG ĐC CHỮ
# SLICE CHỈ DÙNG ĐC BIẾN VỚI SỐ THÔI
print(slice[start:end])

# fym substring?
print(company.startswith('Coding')) # prints true
print(company.startswith('coding'))

