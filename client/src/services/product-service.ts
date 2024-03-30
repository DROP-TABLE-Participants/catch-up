import { AuthApi, Register, TokenObtainPair, TokenRefresh } from "../api";
import { AxiosResponse } from "axios";
import { WebApiService } from "./web-api-service";

export class AuthenticationService extends WebApiService {

    authApi: AuthApi;

  constructor() {
    super();
    this.authApi = new AuthApi();
  }

  public async makeLoginRequest(username: string, password: string): Promise<AxiosResponse<TokenObtainPair, any>> {
    let tokenObtainPair =  {
        username,
        password
    } as TokenObtainPair;
    console.log(tokenObtainPair);

    return await this.authApi.authLoginCreate(tokenObtainPair, this.generateHeader());
  }

  public async makeRegisterRequest(username: string, email: string, password: string, password2: string): Promise<AxiosResponse<Register, any>> {
    let register = {
        username,
        email,
        password,
        password2
    } as Register;

    return await this.authApi.authRegisterCreate(register, this.generateHeader());
  }

  public async renewToken(access: string, refresh: string): Promise<AxiosResponse<TokenRefresh, any>> {
    let tokenRefresh = {
        access,
        refresh,
    } as TokenRefresh;
    return await this.authApi.authRefreshTokenCreate(tokenRefresh, this.generateHeader());
  }
}

const authenticationService = new AuthenticationService();
export default authenticationService;