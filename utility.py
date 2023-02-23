import base64, os, json

files = os.listdir('data/')
master_json=[]

for f in files:
    with open("data/{}".format(f), 'r') as fin:
        lines = [line.strip('\n') + '\r' for line in fin]
        msg = ''
        for ln in lines:
            msg += ln 
        sample_string_bytes = msg.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        hl7_row = {"data": "{}".format(base64_bytes.decode("utf-8"))}
        master_json.append(hl7_row)

result = [json.dumps(record) for record in master_json]
master_ndjson = '\n'.join(result)
with open("output.ndjson", 'w+') as f:
    f.write(master_ndjson)
    f.close()