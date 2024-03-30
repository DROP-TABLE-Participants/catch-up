import { AuthApi, Register, TokenObtainPair, TokenRefresh } from "../api";
import axios, { AxiosPromise, AxiosResponse } from "axios";
import { WebApiService } from "./web-api-service";
import { BASE_PATH } from "../api/base";

export class ProductService extends WebApiService {

  products: Array<any> | null;

  constructor() {
    super();
    this.products = null;
  }

  public async getAllProducts(): Promise<Array<any> | null> {
    if(this.products) {
      return this.products;
    }

    this.products = await axios.get(BASE_PATH + '/api/products/', this.generateHeader());

    return this.products;
  }

  public async createProduct(name: string, image?: Blob): AxiosPromise<any> {
    return await axios.postForm(BASE_PATH + '/api/product/', {name, image_url: image}, this.generateHeader());
  }
}

const productService = new ProductService();
export default productService;