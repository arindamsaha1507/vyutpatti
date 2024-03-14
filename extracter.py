"""उत्सर्गादुपदेशस्य सङ्कलनम्"""

with open("dhaatupaatha.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

data = [d.strip() for d in data]
data = [d for d in data if len(d.split('।')) == 3 and d[-1] == '॥']

NUMBERS = '०१२३४५६७८९'

with open("dhaatu_upadesha", "w", encoding="utf-8") as f:
    for dd in data:
        upadesha = dd.split('।')[2]
        dhaatu = upadesha.split(' ')[1]
        dhaatu = dhaatu[:-1] if dhaatu[-1] == 'ऽ' else dhaatu
        kramaanka = upadesha.split(' ')[-2]
        artha = ' '.join(upadesha.split(' ')[2:-2])
        split = list(d for d in dhaatu)
        f.write(f'{kramaanka} {dhaatu} {artha} {split}\n')
print(len(data))