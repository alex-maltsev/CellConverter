//
//  CollectionTestController.m
//  ConversionTest
//
//  Created by Alexander Maltsev on 3/19/16.
//  Copyright © 2016 self. All rights reserved.
//

#import "CollectionTestController.h"

#define COLLECTION_CELL_XIB_NAME @"CollectionViewCell"
#define COLLECTION_CELL_HEIGHT 50.0

@interface CollectionTestController () <UICollectionViewDataSource, UICollectionViewDelegateFlowLayout>

@property (weak, nonatomic) IBOutlet UICollectionView *collectionView;

@end

@implementation CollectionTestController

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    
    self.collectionView.delegate = self;
    [self.collectionView registerNib:[UINib nibWithNibName:COLLECTION_CELL_XIB_NAME bundle:nil] forCellWithReuseIdentifier:COLLECTION_CELL_XIB_NAME];
}


- (NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section
{
    return 5;
}


- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath
{
    UICollectionViewCell *cell = [self.collectionView dequeueReusableCellWithReuseIdentifier:COLLECTION_CELL_XIB_NAME forIndexPath:indexPath];
    return cell;
}


- (CGSize)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout sizeForItemAtIndexPath:(NSIndexPath *)indexPath
{
    return CGSizeMake(self.view.bounds.size.width, COLLECTION_CELL_HEIGHT);
}

@end
