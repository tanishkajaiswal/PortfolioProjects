/* 
CLEANING DATA IN SQL QUERIES
*/

SELECT *
FROM PortfolioProject..NashvilleHousing

------------------------------------------------------------------------

--STANDARDIZE DATE FORMAT

SELECT SaleDateConverted, CONVERT(Date, SaleDate)
FROM PortfolioProject..NashvilleHousing

UPDATE NashvilleHousing
SET SaleDate=CONVERT(Date, SaleDate)

ALTER TABLE NashvilleHousing
ADD SaleDateConverted DATE;

UPDATE NashvilleHousing
SET SaleDateConverted=CONVERT(Date, SaleDate)

-----------------------------------------------------------------------------------------------

--POPULATE PROPERTY ADDRESS

SELECT *
FROM PortfolioProject..NashvilleHousing
ORDER BY ParcelID

--checking
SELECT a.parcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress
FROM PortfolioProject..NashvilleHousing a
JOIN PortfolioProject..NashvilleHousing b
	ON a.ParcelID=b.ParcelID
	AND a.[UniqueID ]<> b.[UniqueID ]
WHERE a.PropertyAddress is null

--fixing
UPDATE a
SET PropertyAddress=ISNULL(a.propertyAddress, b.PropertyAddress)
FROM PortfolioProject..NashvilleHousing a
JOIN PortfolioProject..NashvilleHousing b
	ON a.ParcelID=b.ParcelID
	AND a.[UniqueID ]<> b.[UniqueID ]



--------------------------------------------------------------------------------------------------------------
--BREAKING OUT ADDRESS IN MULTIPLE COLUMNS

SELECT PropertyAddress
FROM PortfolioProject..NashvilleHousing

SELECT 
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1) as Adddress
,SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+1, LEN(PropertyAddress)) as Address
FROM PortfolioProject..NashvilleHousing

----
ALTER TABLE NashvilleHousing
ADD PropertySplitAddress NVARCHAR(255);

UPDATE NashvilleHousing
SET PropertySplitAddress=SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress)-1)

ALTER TABLE NashvilleHousing
ADD PropertySplitCity NVARCHAR(255);

UPDATE NashvilleHousing
SET PropertySplitCity=SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress)+1, LEN(PropertyAddress))

----
SELECT 
PARSENAME(REPLACE (Owneraddress, ',', '.'),3)
,PARSENAME(REPLACE (Owneraddress, ',' , '.'),2)
,PARSENAME(REPLACE (Owneraddress, ',' , '.'),1)
FROM PortfolioProject.dbo.NashvilleHousing

--

ALTER TABLE NashvilleHousing
ADD OwnerSplitAddress NVARCHAR(255);

UPDATE NashvilleHousing
SET OwnerSplitAddress=PARSENAME(REPLACE (Owneraddress, ',', '.'),3)


ALTER TABLE NashvilleHousing
ADD OwnerSplitCity NVARCHAR(255);

UPDATE NashvilleHousing
SET OwnerSplitCity=PARSENAME(REPLACE (Owneraddress, ',' , '.'),2)


ALTER TABLE NashvilleHousing
ADD OwnerSplitState NVARCHAR(255);

UPDATE NashvilleHousing
SET OwnerSplitState=PARSENAME(REPLACE (Owneraddress, ',' , '.'),1)


-------------------------------------------------------------------------------------------------------------------------------------------------------

--CHANGE Y AND N TO YES AND NO IN "SOLD AS VACANT" FIELD

SELECT DISTINCT(SoldAsVacant), COUNT(SoldAsVacant)
FROM NashvilleHousing
Group by SoldAsVacant
order by 2


SELECT SoldAsVacant
, CASE WHEN SoldAsVacant='Y' THEN 'YES'
	   WHEN SoldAsVacant ='N' THEN 'NO'
	   ELSE SoldAsVacant
	   END
FROM PortfolioProject.dbo.NashvilleHousing


UPDATE NashvilleHousing
SET SoldAsVacant= CASE WHEN SoldAsVacant='Y' THEN 'YES'
	   WHEN SoldAsVacant ='N' THEN 'NO'
	   ELSE SoldAsVacant
	   END


-------------------------------------------------------------------------------------------------------------------------------------

--REMOVE DUPLICATES

WITH RowNumCTE AS(
SELECT *,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
				 PropertYAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY 
				   UniqueID
				   ) row_num
FROM PortfolioProject.dbo.NashvilleHousing
)
DELETE
FROM RowNumCTE
WHERE row_num>1
--ORDER BY PropertyAddress


--------------------------------------------------------------------------------------------------------------------------------------------------------------------

--DELETE UNUSED COLUMNS

ALTER TABLE PortfolioProject.dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate

SELECT *
FROM PortfolioProject.dbo.NashvilleHousing