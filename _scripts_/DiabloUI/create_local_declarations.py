SetType(LocByName("UiDestroy"), "void __cdecl UiDestroy()")
SetType(LocByName("UiTitleDialog"), "void __stdcall UiTitleDialog(int a1)")
SetType(LocByName("UiInitialize"), "void __cdecl UiInitialize()")
SetType(LocByName("UiCopyProtError"), "void __stdcall UiCopyProtError(int a1)")
SetType(LocByName("UiAppActivate"), "void __stdcall UiAppActivate(int a1)")
SetType(LocByName("UiValidPlayerName"), "int __stdcall UiValidPlayerName(char *a1)")
SetType(LocByName("UiSelHeroMultDialog"), "int __stdcall UiSelHeroMultDialog(void *fninfo, void *fncreate, void *fnremove, void *fnstats, int *a5, int *a6, char *name)")
SetType(LocByName("UiSelHeroSingDialog"), "int __stdcall UiSelHeroSingDialog(void *fninfo, void *fncreate, void *fnremove, void *fnstats, int *a5, char *name, int *difficulty)")
SetType(LocByName("UiCreditsDialog"), "void __stdcall UiCreditsDialog(int a1)")
SetType(LocByName("UiMainMenuDialog"), "int __stdcall UiMainMenuDialog(char *name, int *a2, void *fnSound, int a4)")
SetType(LocByName("UiProgressDialog"), "int __stdcall UiProgressDialog(HWND window, char *msg, int a3, void *fnfunc, int a5)")
SetType(LocByName("UiProfileGetString"), "int __cdecl UiProfileGetString()")
SetType(LocByName("UiProfileCallback"), "void __cdecl UiProfileCallback()")
SetType(LocByName("UiProfileDraw"), "void __cdecl UiProfileDraw()")
SetType(LocByName("UiCategoryCallback"), "void __cdecl UiCategoryCallback()")
SetType(LocByName("UiGetDataCallback"), "void __cdecl UiGetDataCallback()")
SetType(LocByName("UiAuthCallback"), "void __cdecl UiAuthCallback()")
SetType(LocByName("UiSoundCallback"), "void __cdecl UiSoundCallback()")
SetType(LocByName("UiMessageBoxCallback"), "void __cdecl UiMessageBoxCallback()")
SetType(LocByName("UiDrawDescCallback"), "void __cdecl UiDrawDescCallback()")
SetType(LocByName("UiCreateGameCallback"), "void __cdecl UiCreateGameCallback()")
SetType(LocByName("UiArtCallback"), "BOOL __cdecl UiArtCallback(int connType, unsigned int artIndex, PALETTEENTRY *palette, void *destBuffer)")
SetType(LocByName("UiSelectGame"), "int __stdcall UiSelectGame(int a1, _SNETPROGRAMDATA *client_info, _SNETPLAYERDATA *user_info, _SNETUIDATA *ui_info, _SNETVERSIONDATA *file_info, int *a6)")
SetType(LocByName("UiSelectProvider"), "int __stdcall UiSelectProvider(int a1, _SNETPROGRAMDATA *client_info, _SNETPLAYERDATA *user_info, _SNETUIDATA *ui_info, _SNETVERSIONDATA *file_info, int *type)")
SetType(LocByName("UiCreatePlayerDescription"), "int __stdcall UiCreatePlayerDescription(_uiheroinfo *info, int mode, char *desc)")
SetType(LocByName("UiSetupPlayerInfo"), "int __stdcall UiSetupPlayerInfo(char *str, _uiheroinfo *info, int mode)")
