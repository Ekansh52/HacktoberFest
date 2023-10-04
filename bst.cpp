#include<bits/stdc++.h>
using namespace std;
struct bst{
  int data;
  bst *left;
  bst *right;
};
bst *root=NULL;

void insert(int val)
{
  bst *ptr,*nptr,*temp;
  ptr=new bst;
  ptr->data=val;
  ptr->left=NULL;
  ptr->right=NULL;
  if(root==NULL)
  {
    cout<<"Added to Node: "<<ptr->data<<endl;
    root=ptr;
  }
  else
  {
    cout<<"\n";
    nptr=root;
    while(nptr!=NULL)
    {
      if(val<=nptr->data)
    {
      temp=nptr;
      cout<<temp->data<<"skipped ";
      nptr=nptr->left;
    }
    else
    {
      temp=nptr;
      cout<<temp->data<<"skipped ";
      nptr=nptr->right;
    }
    }
    if(val<=temp->data)
    {
      cout<<"Added to left "<<ptr->data;
      temp->left=ptr;
    }

    else
    {
      cout<<"Added to right "<<ptr->data;
      temp->right=ptr;
    }
  }
}

void search(int val)
{
  bst *ptr;
  ptr=root;
  int s=0;
  while(ptr!=NULL)
  {
    if(ptr->data==val)
    {
      s=1;
      break;
    }
    else if(val<=ptr->data)
    {
      ptr=ptr->left;
    }
    else
      ptr=ptr->right;
  }
  if(s==1)
    cout<<"\nFound";
  else
    cout<<"\nNot Found";

}

void findmin()
{
  bst *ptr;
  ptr=root;
  while(ptr->left!=NULL)
    ptr=ptr->left;
  cout<<"\nMinimum ele : "<<ptr->data;
}

void findmax()
{
  bst *ptr;
  ptr=root;
  while(ptr->right!=NULL)
    ptr=ptr->right;
  cout<<"\nMaximum ele : "<<ptr->data;
}

void bfs()
{
  queue<bst*> q;
  bst *ptr,*curr;
  ptr=root;
  q.push(ptr);
  cout<<"\n";
  while(!q.empty())
  {
    curr=q.front();
    cout<<curr->data<<" ";
    if(curr->left!=NULL)
      q.push(curr->left);
    if(curr->right!=NULL)
      q.push(curr->right);
    q.pop();
  }
}

void inorder(bst *root)
{
  if(root==NULL)
    return;
  inorder(root->left);
  cout<<root->data<<" ";
  inorder(root->right);
}

void preorder(bst *root)
{
  if(root==NULL)
    return;
  cout<<root->data<<" ";
  preorder(root->left);
  preorder(root->right);
}

void postorder(bst *root)
{
  if(root==NULL)
    return;
  postorder(root->left);
  postorder(root->right);
  cout<<root->data<<" ";
}

int main()
{
  insert(8);
  insert(3);
  insert(10);
  insert(14);
  insert(1);
  insert(6);
  insert(4);
  insert(7);
  insert(13);
  search(6);
  search(2);
  search(10);
  search(9);
  search(23);
  findmin();
  findmax();
  bfs();
  cout<<"\nInorder: ";
  inorder(root);
  cout<<"\nPreorder: ";
  preorder(root);
  cout<<"\nPostorder: ";
  postorder(root);
  return 0;
}