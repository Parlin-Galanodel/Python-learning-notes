/*
	Node
*/
typedef struct node *node_ptr;		//typedef
struct node{
	element_type element;			//cargo
	node_ptr next;					//a pointer to another node
};

/*
	is_empty, is_last and find method
*/
typedef node_ptr LIST;
typedef node_ptr position;

int is_empty(LIST L):{				//LIST L is Header of the list
	return (LIST->next == NULL);	// no element in header
};

int is_last(position p, LIST L){
	return (p->next == NULL);
};

position find(element_type x, LIST L){
	position p;
	p = L->next;
	while((p != NULL) && (p->element != x))
		p=p->next;
	return p;
}

/*
	delete a node
*/
void delete(element_type x, LIST L){
	position p, tmp_cell;
	p=find_previous(x,L);
	if (p->next != NULL){
		tmp_cell = p->next;
		p->next = tmp_cell->next;
		free(tmp_cell);
	}
}

position find_previous(element_type x, LIST L){
	position p;
	p=L;
	while((p->next != NULL)&&(p->next->element !=x)){
		p=p->next;
	}
	return p;
}

/*
	Insert
*/
void insert(element_type x, LIST L, position p){
	position tmp_cell;
	tmp_cell = (position) malloc ( sizeof(structure));
	if (tmp_cell == NULL)
		fatal_error("Out of space!!");
	else{
		tmp_cell->element=x;
		tmp_cell->next=p->next;
		p->next=tmp_cell;
	}
}

/*
	delete the list
*/
void delete_list(LIST L){
	position p, tmp;
	p=L->next;
	L->next=NULL;
	while (p !=NULL){
		tmp = p->next;
		free(p);					//p is allocated by malloc
									//and could only be released 
									//by free()
		p=tmp;
	}
}