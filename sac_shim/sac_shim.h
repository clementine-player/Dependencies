/* This file is part of Clementine.

   Clementine is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   Clementine is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with Clementine.  If not, see <http://www.gnu.org/licenses/>.
*/

// This is a wrapper around the CSecureChannelClient class from scclient.h
// in the Windows Media Device Manager SDK.  It exports a C API that can be
// used by applications compiled with GCC. Compile it with MSVC 6, remembering
// to add "mssachlp.lib" "MSVCRT.lib" to the linker command line.

#ifndef SAC_SHIM_H
#define SAC_SHIM_H

#include <wtypes.h>
#include <sac.h>

class CSecureChannelClient;
struct IComponentAuthenticate;
typedef CSecureChannelClient* SacHandle;

#ifndef SAC_MAC_LEN
#define SAC_MAC_LEN 8
#endif

extern "C" {

SacHandle CSecureChannelClient_New();
void CSecureChannelClient_Free(SacHandle handle);

HRESULT CSecureChannelClient_SetCertificate(SacHandle handle, DWORD flags, BYTE* cert, DWORD cert_len, BYTE* key, DWORD key_len);
void CSecureChannelClient_SetInterface(SacHandle handle, IComponentAuthenticate* auth);
HRESULT CSecureChannelClient_Authenticate(SacHandle handle, DWORD id);
HRESULT CSecureChannelClient_EncryptParam(SacHandle handle, BYTE* data, DWORD len);
HRESULT CSecureChannelClient_DecryptParam(SacHandle handle, BYTE* data, DWORD len);
HRESULT CSecureChannelClient_MACInit(SacHandle handle, HMAC* mac);
HRESULT CSecureChannelClient_MACUpdate(SacHandle handle, HMAC mac, BYTE* data, DWORD len);
HRESULT CSecureChannelClient_MACFinal(SacHandle handle, HMAC mac, BYTE* data);
HRESULT CSecureChannelClient_GetAppSec(SacHandle handle, DWORD* local_sec, DWORD* remote_sec);
HRESULT CSecureChannelClient_GetSessionKey(SacHandle handle, BYTE* key);
HRESULT CSecureChannelClient_SetSessionKey(SacHandle handle, BYTE* key);
HRESULT CSecureChannelClient_GetRemoteAppCert(SacHandle handle, BYTE* cert, DWORD* len);
BOOL CSecureChannelClient_IsAuthenticated(SacHandle handle);

}

#endif
