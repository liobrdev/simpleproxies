// Misc
export interface IAction {
  type: string;
  [key: string]: any;
}

export interface IBreadcrumbListItem {
  '@type': string;
  position: number;
  name: string;
  item: string;
}

export interface IButton {
  action: IAction;
  text: string;
}

export interface IErrorMsg {
  id: string;
  msg: string;
}

export interface IErrorInfo {
  [key: string]: IErrorMsg[];
}

export interface IRoute {
  path: string;
  name?: string;
}
