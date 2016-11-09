# engine.cpp

## 0x52B97C

### seed

```c
// seed represents the global seed of the game.
//
// PSX ref: 0x8011C7C4
// PSX def: long sglGameSeed
int32_t seed;
```

## 0x52B980

### mem_mutex

```c
// mem_mutex is a mutex which protects memory operations from race conditions.
CRITICAL_SECTION mem_mutex;
```
