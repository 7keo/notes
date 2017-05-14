// address: 0x456A16
//
// sha1_reset resets the global SHA-1 contexts.
void sha1_reset();

// address: 0x456A2B
//
// sha1_final copies the message digest of the given SHA-1 context to dst.
void __fastcall sha1_final(int ctx_id, uint8_t (*dst)[20]);

// address: 0x456A4D
//
// sha1 adds the 64-byte block of data to the running hash of the given SHA-1
// context and stores the final message digest in dst.
void __fastcall sha1(int ctx_id, const uint8_t *data, uint8_t (*dst)[20]);

// address: 0x456A73
//
// sha1_update adds the data to the running hash of the given SHA-1 context.
void __fastcall sha1_update(Sha1Ctx *ctx, const uint8_t *data, int len);

// address: 0x456AC4
//
// sha1_transform performs a SHA-1 transformation on the 64-byte block of the
// given SHA-1 context.
void __fastcall sha1_transform(Sha1Ctx *ctx);

// address: 0x456C82
//
// sha1_init initializes the given SHA-1 context.
void __fastcall sha1_init(int ctx_id);

