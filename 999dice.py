import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))