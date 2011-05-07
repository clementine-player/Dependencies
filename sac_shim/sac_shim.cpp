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

#include "sac_shim.h"

#include <scclient.h>

SacHandle CSecureChannelClient_New() {
  return new CSecureChannelClient;
}

void CSecureChannelClient_Free(SacHandle handle) {
  delete handle;
}

HRESULT CSecureChannelClient_SetCertificate(SacHandle handle, DWORD flags, BYTE* cert, DWORD cert_len, BYTE* key, DWORD key_len) {
  return handle->SetCertificate(flags, cert, cert_len, key, key_len);
}

void CSecureChannelClient_SetInterface(SacHandle handle, IComponentAuthenticate* auth) {
  handle->SetInterface(auth);
}

HRESULT CSecureChannelClient_Authenticate(SacHandle handle, DWORD id) {
  return handle->Authenticate(id);
}

HRESULT CSecureChannelClient_EncryptParam(SacHandle handle, BYTE* data, DWORD len) {
  return handle->EncryptParam(data, len);
}

HRESULT CSecureChannelClient_DecryptParam(SacHandle handle, BYTE* data, DWORD len) {
  return handle->DecryptParam(data, len);
}

HRESULT CSecureChannelClient_MACInit(SacHandle handle, HMAC* mac) {
  return handle->MACInit(mac);
}

HRESULT CSecureChannelClient_MACUpdate(SacHandle handle, HMAC mac, BYTE* data, DWORD len) {
  return handle->MACUpdate(mac, data, len);
}

HRESULT CSecureChannelClient_MACFinal(SacHandle handle, HMAC mac, BYTE* data) {
  return handle->MACFinal(mac, data);
}

HRESULT CSecureChannelClient_GetAppSec(SacHandle handle, DWORD* local_sec, DWORD* remote_sec) {
  return handle->GetAppSec(local_sec, remote_sec);
}

HRESULT CSecureChannelClient_GetSessionKey(SacHandle handle, BYTE* key) {
  return handle->GetSessionKey(key);
}

HRESULT CSecureChannelClient_SetSessionKey(SacHandle handle, BYTE* key) {
  return handle->SetSessionKey(key);
}

HRESULT CSecureChannelClient_GetRemoteAppCert(SacHandle handle, BYTE* cert, DWORD* len) {
  return handle->GetRemoteAppCert(cert, len);
}

BOOL CSecureChannelClient_IsAuthenticated(SacHandle handle) {  
  return handle->fIsAuthenticated();
}

