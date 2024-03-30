import {
  LOCAL_STORAGE_ACCESS_TOKEN_KEY,
  LOCAL_STORAGE_REFRESH_TOKEN_KEY,
  LOCAL_STORAGE_EXPIRATION_DATE_KEY
} from "../shared/constants";

class StorageService {
  public retrieveAccessToken(): string | null {
    try {
      const accessToken = localStorage.getItem(LOCAL_STORAGE_ACCESS_TOKEN_KEY);
      if (!accessToken) {
        return null;
      }
      return accessToken;
    } catch (e) {
      localStorage.removeItem(LOCAL_STORAGE_ACCESS_TOKEN_KEY);
      return null;
    }
  }

  public saveAccessToken(accessToken: string | null): void {
    if (accessToken) {
      localStorage.setItem(LOCAL_STORAGE_ACCESS_TOKEN_KEY, accessToken);
    } else {
      localStorage.removeItem(LOCAL_STORAGE_ACCESS_TOKEN_KEY);
    }
  }

  public retrieveRefreshToken(): string | null {
    try {
      const refreshToken = localStorage.getItem(LOCAL_STORAGE_REFRESH_TOKEN_KEY);
      if (!refreshToken) {
        return null;
      }
      return refreshToken;
    } catch (e) {
      localStorage.removeItem(LOCAL_STORAGE_REFRESH_TOKEN_KEY);
      return null;
    }
  }

  public saveRefreshToken(refreshToken: string | null): void {
    if (refreshToken) {
      localStorage.setItem(LOCAL_STORAGE_REFRESH_TOKEN_KEY, refreshToken);
    } else {
      localStorage.removeItem(LOCAL_STORAGE_REFRESH_TOKEN_KEY);
    }
  }

  saveTokenExpiresDate(date: string | null): void {
    if (date) {
      localStorage.setItem(LOCAL_STORAGE_EXPIRATION_DATE_KEY, date);
    } else {
      localStorage.removeItem(LOCAL_STORAGE_EXPIRATION_DATE_KEY);
    }
  }

  retrieveTokenExpiresDate(): Date | null {
    try {
      const date = localStorage.getItem(LOCAL_STORAGE_EXPIRATION_DATE_KEY);
      if (!date) {
        return null;
      }
      return new Date(date);
    } catch (e) {
      localStorage.removeItem(LOCAL_STORAGE_EXPIRATION_DATE_KEY);
      return null;
    }
  }


  checkForUserLogin(): boolean {
    const token = this.retrieveAccessToken();
    const refreshToken = this.retrieveRefreshToken();
    const expirationDate = this.retrieveTokenExpiresDate();
    if (token && refreshToken && expirationDate) {
      return true;
    }
    return false;
  }

  deleteUserData(): void {
    localStorage.removeItem(LOCAL_STORAGE_ACCESS_TOKEN_KEY);
    localStorage.removeItem(LOCAL_STORAGE_REFRESH_TOKEN_KEY);
    localStorage.removeItem(LOCAL_STORAGE_EXPIRATION_DATE_KEY);
  }
}

const storageService = new StorageService();
export default storageService;